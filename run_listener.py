#!/usr/bin/python
from sdust_oj.judgeServer.listener import *
print "Listener is ready ....."
listener = Listener()
listener.server_forever()
