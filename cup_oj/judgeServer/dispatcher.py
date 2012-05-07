#!/usr/bin/python
# encoding=utf8
'''
Created on May 2, 2012

@author: Lee Guojun
@功能:消息队列分派器，等待来自judgeClient的请求，每来一个请求，就从相应的队列中取出提交消息并
传给judgeClient，等到收到来自judgeClient的完成相应时就发给judgeServer一个对应的ACK，然后judgeServer
才可以从队列中把这个消息free掉。
这是一个消费者。
@性质:1.JudgeServer的分派器部件。2.RabbitMQClient。3.RPCServer
@改进:是否应该使用forking 或者 threading /
'''
'''
from cup_oj.sa_conn import DeclarativeBase, metadata, Session
import sys
import pika
import time 
import os
'''