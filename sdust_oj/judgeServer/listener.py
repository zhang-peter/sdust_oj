#!/usr/bin/python
# encoding=utf8
'''
Created on Apr 28, 2012

@author: Lee Guojun
@功能:数据库监听器，每个一段时间访问数据库，把不是终结状态的提交取出放到任务队列中，等待
来自客户端的请求将相应的提交取走。这是一个生产者。
@性质:1.JudgeServer的监听器部件。2.RabbitMQServer
'''

from sdust_oj.sa_conn import Session
from sdust_oj.status import *

from sdust_oj.tables.auth import User
from sdust_oj.tables.problem import Problem, Submission

import sys
import pika
import time 

"""
RabbitMQ运行在JudgeServer上，包括RabbitMQServer和RabbitMQClient,这样设计是为了层次划分
清楚，未来维护也会简单易行。当然也可以像http://www.rabbitmq.com/tutorials/tutorial-six-python.html
讲到的这样，写成远程过程调用的模式，但是这样子做明显封装不够，要求维护时对整体的设计要相当清楚。

要持久化消息的步骤如下：
1.将交换机设成 durable
2.将队列设成 durable
3.将消息的 Delivery Mode 设置成2 (持久的persistent）
"""


FETCHNUMBER = 50 				# 一次从数据库中取出的提交数量
UNABLE_TO_CONNECT = 1
UNABLE_TO_GET_CHANNEL = 2
DELAY_TIME = 2					# 数据库监听时间，以秒为单位，参见python>>help()>>time
OnLineJudgeStatus = ["Pending","Keyword_checking","Compiling","Running","Output_checking"]
EndStatus = [keyword_checked_error,compiled_error,compiled_error,runtime_error,memory_over_error,presentation_error,fetched]
FetchStatus = [pending, keyword_check_ok, compile_ok, run_ok, output_check_ok]

from sdust_oj.constant import judge_flows
class Listener:
	connection = None
	channel = None
	flag = False
	
	
	def __init__(self,host="localhost"):
		"""
		初始化就保持与RabbitMQ的链接，一直到服务器停止，若链接不上，则停止程序运行
		"""
		if self.getConnection(host) == False:
			sys.exit(UNABLE_TO_CONNECT)
		self.getChannel()

	def getConnection(self,host="localhost"):
		"""
		链接RabiitMQ，获得connection
		"""
		try:
			self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
			self.flag = True
		except Exception as e:
			print "Unable to Connect RabbitMQ"
			print e
		return self.flag
	
	def getChannel(self):
		"""
		获得channel
		"""
		try:
			self.channel = self.connection.channel()
		except Exception as e:
			print "Unable to get RabbitMQ channel "
			print e
	
	def bindByStatus(self,status=None):
		que = status + "_queue"
		exc = status + "_exchange"
		self.channel.queue_declare(queue=que,			# ！！！
						durable=True,					# 重启之后会重新建立
						exclusive=False,				# 如果设置成True，只有创建这个队列的消费者程序才允许连接到该队列。这种队列对于这个消费者程序是私有的
						auto_delete=False,				# 最后一个消费者断开的时候不会自动删除	
						)
		self.channel.exchange_declare(exchange=exc,		# !!!
						type="direct",
						durable=True,
						auto_delete=False,
						)
		self.channel.queue_bind(queue=que,
						exchange=exc,					#
						routing_key=status,				# 根据状态路由
						)

	def getSession(self):
		"""
		或得数据库session
		"""
		try:
			session = Session()	# 开启与数据库的链接
		except Exception as e:
			print "Open Session Error"
			print e
		return session
		
	def closeSession(self,session):
		try:
			session.close()		# 关闭与数据库的链接
		except Exception as e:
			print "Session close Error"
			print e
	
	def getMessages(self):
		"""
		从数据库中获取一定数量的未终结状态的提交。NOTE 返回的是query
		"""
		session = self.getSession()	
		session.expire_on_commit = False
		submissionMessages = []
		msg=[]
		try:
			submissionMessages = session.query(Submission).filter(Submission.status.in_(FetchStatus)).limit(FETCHNUMBER)
			for message in submissionMessages:
				message.pre_status = message.status 
				message.status = fetched
				msg.append(message)
				print "Current Message Status:%d" % message.status
				print "sending to the dispatcher...Ok"
			session.commit()
			#session.add_all(submissionMessages)
		except Exception as e:
			print "Exception raised in GetMessages()"
			print e	
		finally:
			self.closeSession(session)
		
		print 'len of messages=%d'%(len(msg))
		return msg
		
	def getNextStauts(self,flow,curStatus):
		"""
		index = flow.index(curStatus)
		if index + 1 > len(flow):
			return -1
		else:
			return flow[index+1]
		"""
		flow_id = 0
		for f in judge_flows:
			if curStatus == f[5]:
				flow_id = f[0]
				break
		try:
			print "flow_id: " + str(flow_id)
			if curStatus == pending:
				next_flow_id = flow[0]
			else:
				next_flow_id = flow[flow.index(str(flow_id)) + 1]
			for f in judge_flows:
				if next_flow_id == str(f[0]):
					return f[6]
		except IndexError:
			return -1

	def public(self,messages):
		"""
		把消息发送到消息队列中去。
		@messages 从数据库中得到的query集
		"""	
		session = self.getSession()
		for message in messages:
			flow_string = str(session.query(Problem).get(message.problem_id).judge_flow)
			flow = flow_string.split('$')
			del flow[0]
			status = self.getNextStauts(flow, message.pre_status)
			if status == -1:
				session.query(Submission).get(message.id).status = accept
				session.query(Problem).filter_by(id = message.problem_id).update({"accept": Problem.accept+1})
				session.query(User).filter_by(id = message.user_id).update({"accept": User.submit+1})
				session.commit()
				continue
			exc = status + "_exchange"
			key = status
			print 'in listener publish the message....now the message->id =%s to %s' % (str(message.id), exc)
			self.channel.basic_publish(exchange=exc,
									routing_key=key,
									body=str(message.id),
		      						properties=pika.BasicProperties(
									delivery_mode = 1,		# 2 Make message persistent!
		     						))
		self.closeSession(session)

	def listen(self):
		"""	
		1.定时监听数据库，
		2.发现未完成状态就提取出来
		3.插入到消息队列中去。
		"""
	# 若不需要和RabbitMQ 保持长链接，改改这的代码即可
		while True:
			time.sleep(DELAY_TIME)
			submissionMessages = self.getMessages()
			self.public(submissionMessages)
	
	def server_forever(self):
		for status in OnLineJudgeStatus:
			self.bindByStatus(status)
		self.listen()


def main():
	listener = Listener()
	listener.server_forever()
	
#main()





