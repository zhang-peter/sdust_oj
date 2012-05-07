#!/usr/bin/python
# encoding=utf8

'''
Created on May 2, 2012
远程过程调用服务器RPCServer
@author: Lee Guojun
@功能:1.消息队列分派器，等待来自judgeClient的请求，每来一个请求，就从相应的队列中取出提交消息并
传给judgeClient，等到收到来自judgeClient的完成相应时就发给judgeServer一个对应的ACK，然后judgeServer
才可以从队列中把这个消息free掉。
2.收集来自JudgeClient的处理结果，并把它写到数据库中。

@性质:1.JudgeServer的RPCServer。2.RabbitMQClient。
'''
from cup_oj.sa_conn import DeclarativeBase, metadata, Session
from SimpleXMLRPCServer import SimpleXMLRPCServer,SimpleXMLRPCRequestHandler        # \
from SocketServer import ForkingMixIn                                               # | RPCServer 
import sys      
import pika     # rabbitMQ 链接库
import time 
import os

UNABLE_TO_CONNECT = 1
UNABLE_TO_GET_CHANNEL = 2
OnLineJudgeStatus = ["Pending","KeyWordsChecking","Compiling","Running",]

class RPCServer:
    connection = None
    channel = None
    flag = False
    host = "localhost"
    port = 8765
    serveraddr = (host,port)
    
    """
    一下几个函数是相对于RabbitMQ来说，是客户端
    """
    def getConnection(self,host="localhost"):
        """
        链接RabiitMQ，获得connection
        """
        self.host = host
        try:
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.host))
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
            
    def __init__(self,host="localhost"):
        """
        初始化就保持与RabbitMQ的链接，一直到服务器停止，若链接不上，则停止程序运行
        """
        if self.getConnection(host) == False:
            sys.exit(UNABLE_TO_CONNECT)
        self.getChannel()
    
    def bindByStatus(self,status=None):
        que = status + "_queue"
        exc = status + "_exchange"
        #在这里又重新声明了队列是因为RabbitMQ的server端和client端不知道谁先运行
        self.channel.queue_declare(queue=que,               
                        durable=True,                    
                        exclusive=False,                
                        auto_delete=False,                
                        )
        self.channel.queue_bind(queue=que,                    
                        exchange=exc,                   
                        routing_key=status,                
                        )

    def callback(self, method, properties, message):
        #  弃用
        print " [x] %r" % (message.status,)
    
    def bind(self):
        for status in OnLineJudgeStatus:
            self.bindByStatus(status)
    
    def onRequest(self,status):
        """
        这是提供给RPClient的接口,根据状态返回请求
        eg： onRequest("Pending") or onRequest("Compiling")
        """
        que = status + "_queue"
        method_frame, header_frame, body = self.channel.basic_get(queue=que)
        if method_frame.NAME == 'Basic.GetEmpty':
            print 'Receive empty message.'
        else:
            #print body
            self.channel.basic_ack(delivery_tag=method_frame.delivery_tag)
            return body # message(submission)

    pass
    
class ForkingServer(ForkingMixIn,SimpleXMLRPCServer):
    pass

def main():
    if __name__  == '__main__':
        serveraddr =('localhost',8765)
        server = ForkingServer(serveraddr,SimpleXMLRPCRequestHandler)
        server.register_multicall_functions()
        server.register_instance(RPCServer())
        server.register_introspection_functions()
        print "[x] Waiting ..."
        server.serve_forever()
    else:
        print __name__ + "Called by JudgeServer..."
        
main()


