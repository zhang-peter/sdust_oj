#!/usr/bin/python
# encoding=utf8
'''
Created on May 4, 2012

@author: Lee Guojun
@功能:远程过程调用的一个客户端，处理那些是pending状态的提交。该进程请求
onRequest("Pending"),会得到一个处于pending状态的提交，然后对他进行处理
然后将结果返回给RPCServer。

'''

import os,sys,time
import xmlrpclib

status = "Pending"

def handlePending():
    url = "http://localhost:8765"
    server = xmlrpclib.ServerProxy(url)
    message = server.onRequest(status)
    # 处理pending状态的提交
    # pass
    # 处理完之后把message传给服务器
    
    
    