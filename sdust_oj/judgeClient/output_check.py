# encoding=utf8
'''
Created on May 7, 2012

@author: king
@功能:远程过程调用的一个客户端，处理那些是pending状态的提交。该进程请求
onRequest("Pending"),会得到一个处于pending状态的提交，然后对他进行处理
然后将结果返回给RPCServer。
'''


import os,sys,time
import xmlrpclib
from sdust_oj.tables.auth import User
from sdust_oj.tables.problem import Submission,Problem
import pickle
import time

from sdust_oj import settings

from sdust_oj import status as STATUS

from sdust_oj.judgeClient.judge import useful_types
from sdust_oj.judgeClient.judge import output_check_main

def handleOutputChecking(RPCUri="http://127.0.0.1",port="8765"):
    url = RPCUri+":"+port
    server = xmlrpclib.ServerProxy(url,allow_none=True)
    
    while True:   
        try: 
            id = server.onRequest("Output_checking")
            print 'id = %s'%id
            if id is None:
                print "没有任务，退出！"
                time.sleep(3)
                continue
            server.updateStatusById(id, STATUS.output_checking)
                
        except xmlrpclib.Fault, err:
            print "A fault occurred"
            print "Fault code: %d" % err.faultCode
            print "Fault string: %s" % err.faultString 
        
        try: 
            meta_id, io_list = server.getMetaIOByID(id)
        except xmlrpclib.Fault, err:
            print "A fault occurred"
            print "Fault code: %d" % err.faultCode
            print "Fault string: %s" % err.faultString 
        
        work_path = os.path.join(settings.ROOT_PATH, "judge_root", "work", str(id))
        if not os.path.exists(work_path):
            os.makedirs(work_path)
        os.chdir(work_path)
        

        s = output_check_main(meta_id, io_list, id)
        print "output check return status: %s" % s
        server.updateStatusById(id, s)
        
        time.sleep(0.5)
        