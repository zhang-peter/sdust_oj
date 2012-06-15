# coding=UTF8

from sqlalchemy import Table, Column, ForeignKey, Integer, String, Boolean, \
    DateTime
from sqlalchemy.orm import mapper, relationship
from datetime import datetime

from sdust_oj.sa_conn import metadata

user = Table("User", metadata,
             Column("id", Integer, primary_key=True),
             Column("username", String(50), nullable=False, unique=True),
             Column("password", String(100), nullable=False),
             Column("nickname", String(50), nullable=False), 
             Column("email", String(50), nullable=False),
             Column("is_superuser", Boolean, nullable=False, default=False),
             Column("is_active", Boolean, nullable=False, default=False),
             Column("reg_time", DateTime, nullable=False, default=datetime.now()),
             Column("last_login", DateTime, nullable=False, default=datetime.now()),
             Column("submit", Integer, nullable=False, default=0),
             Column("accept", Integer, nullable=False, default=0),
       )

permission = Table("Permission", metadata,
             Column("id", Integer, primary_key=True),
             Column("name", String(50), nullable=False, unique=True),
       )

group = Table("Group", metadata,
             Column("id", Integer, primary_key=True),
             Column("name", String(50), nullable=False, unique=True),
       )


permissionGroup = Table("permissionGroup", metadata,
    Column("permission_id", Integer, ForeignKey('Permission.id'), primary_key=True, nullable=False),
    Column("group_id", Integer, ForeignKey('Group.id'), primary_key=True, nullable=False),
)

userGroup = Table("userGroup", metadata,
    Column("user_id", Integer, ForeignKey('User.id'), primary_key=True, nullable=False),
    Column("group_id", Integer, ForeignKey('Group.id'), primary_key=True, nullable=False),
)

userPermission = Table("userPermission", metadata,
    Column("user_id", Integer, ForeignKey('User.id'), primary_key=True, nullable=False),
    Column("permission_id", Integer, ForeignKey('Permission.id'), primary_key=True, nullable=False),
)

metadata.create_all() # if tables don't exit, create them.

from sdust_oj.models.auth import User, Permission, Group
from sdust_oj.tables.problem import Submission

mapper(User, user, properties={
    "groups":relationship(Group, secondary=userGroup, backref="users"),
    "permissions":relationship(Permission, secondary=userPermission, backref="users"),
    "submissions":relationship(Submission, backref="user")
})
mapper(Permission, permission, properties={
    "groups":relationship(Group, secondary=permissionGroup, backref="permissions")
})
mapper(Group, group)


def is_anonymous(self):
    """
    Always returns False. This is a way of comparing User objects to
    anonymous users.
    """
    return False

User.is_anonymous = is_anonymous

def is_authenticated(self):
    """
    Always return True. This is a way to tell if the user has been
    authenticated in templates.
    """
    return True

User.is_authenticated = is_authenticated

from sdust_oj.auth.hashers import make_password, check_password as check_password_raw
def set_password(self, raw_password):
    self.password = make_password(raw_password)
    
User.set_password = set_password
    
from sdust_oj.sa_conn import Session
def check_password(self, raw_password):
    """
    Returns a boolean of whether the raw_password was correct. Handles
    hashing formats behind the scenes.
    """
    def setter(raw_password):
        self.set_password(raw_password)
        session = Session()
        session.merge(self)
        session.commit()
        session.close()
    return check_password_raw(raw_password, self.password, setter)

User.check_password = check_password
