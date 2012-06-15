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
from sdust_oj.judgeClient.judge import compile
def handleCompiling(RPCUri="http://127.0.0.1",port="8765"):
    url = RPCUri+":"+port
    server = xmlrpclib.ServerProxy(url,allow_none=True)
    
    while True:   
        try: 
            id = server.onRequest("Compiling")
            print 'id = %s'%id
            if id is None:
                print "没有任务，退出！"
                time.sleep(3)
                continue
            server.updateStatusById(id, STATUS.compiling)
                
        except xmlrpclib.Fault, err:
            print "A fault occurred"
            print "Fault code: %d" % err.faultCode
            print "Fault string: %s" % err.faultString 
        
        try: 
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
        f = open(src_path, "w+")
        f.write(task.code)
        f.close()

        s = compile(src_path)
        print "compile return status: %s" % s
        server.updateStatusById(id, s)
        
        time.sleep(0.5)
        
        # 处理Compiling状态的提交
        # pass
        # 处理完之后把message传给服务器
        #messageSubmission.status = "compiled"
        #server.sendBack(messageSubmission)
    

#handleCompiling())
    #print msg['id']