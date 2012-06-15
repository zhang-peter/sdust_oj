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
from sdust_oj.judgeClient.judge import run_main

def handleRunning(RPCUri="http://127.0.0.1",port="8765"):
    url = RPCUri+":"+port
    server = xmlrpclib.ServerProxy(url,allow_none=True)
    
    while True:   
        try: 
            id = server.onRequest("Running")
            print 'id = %s'%id
            if id is None:
                print "没有任务，退出！"
                time.sleep(3)
                continue
            server.updateStatusById(id, STATUS.running)
                
        except xmlrpclib.Fault, err:
            print "A fault occurred"
            print "Fault code: %d" % err.faultCode
            print "Fault string: %s" % err.faultString 
        
        try: 
            meta_id, io_list = server.getMetaIOByID(id)
            b = server.getSubmissionById(id)
            b = b.replace("\n\\u000a", "\\u000a")  
            task = pickle.loads(b)
        except xmlrpclib.Fault, err:
            print "A fault occurred"
            print "Fault code: %d" % err.faultCode
            print "Fault string: %s" % err.faultString 
        print 'task.id=%d'% task.id
        
        work_path = os.path.join(settings.ROOT_PATH, "judge_root", "work", str(task.id))
        if not os.path.exists(work_path):
            os.makedirs(work_path)
        os.chdir(work_path)
        
        src_path = os.path.join(work_path, "Main." + str(useful_types[task.code_type]))

        s, mm, tt = run_main(meta_id, io_list, id, src_path)
        print "run return status: %s, memory:%d, time:%d" % (s, mm, tt)
        server.updateStatusAndMTById(id, s, mm, tt)
        
        time.sleep(0.5)
        