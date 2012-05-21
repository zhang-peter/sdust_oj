# coding=UTF8

from datetime import datetime

class User(object):
    """
    Users port from Django Users
    """
    
    def __init__(self, username="", password="", nickname="",
                 email="", is_superuser=False, is_active=False, reg_time=datetime.now(),
                 last_login=datetime.now(), submit=0, accept=0):
        self.username = username
        self.password = password
        self.nickname = nickname
        self.email = email
        self.is_superuser = is_superuser
        self.is_active = is_active
        self.reg_time = reg_time
        self.last_login = last_login
        self.submit = submit
        self.accept = accept
    
class Permission(object):
    
    def __init__(self, name=""):
        self.name = name
        
class Group(object):
    
    def __init__(self, name=""):
        self.name = name