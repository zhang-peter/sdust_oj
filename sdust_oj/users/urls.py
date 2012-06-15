'''
Created on Jun 13, 2012

@author: jingyong
'''

from sdust_oj.users.views import *

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^user_info/$', user_info, name='user_info'),                 
)
