from sqlalchemy import *
from sqlalchemy.orm import relation

from cup_oj.auth.hashers import make_password, check_password
from cup_oj.sa_conn import DeclarativeBase, metadata, Session

permissionGroup = Table(u'permissionGroup', metadata,
    Column(u'permission_id', INTEGER(), ForeignKey('Permission.id'), primary_key=True, nullable=False),
    Column(u'group_id', INTEGER(), ForeignKey('TGroup.id'), primary_key=True, nullable=False),
)

userGroup = Table(u'userGroup', metadata,
    Column(u'user_id', INTEGER(), ForeignKey('User.id'), primary_key=True, nullable=False),
    Column(u'group_id', INTEGER(), ForeignKey('TGroup.id'), primary_key=True, nullable=False),
)

class Permission(DeclarativeBase):
    __tablename__ = 'Permission'

    __table_args__ = {}

    #column definitions
    id = Column(u'id', INTEGER(), primary_key=True, nullable=False)
    name = Column(u'name', INTEGER())

    #relation definitions
    TGroups = relation('TgRoup', primaryjoin='Permission.id==permissionGroup.c.permission_id', secondary=permissionGroup, secondaryjoin='permissionGroup.c.group_id==TgRoup.id')


class TgRoup(DeclarativeBase):
    __tablename__ = 'TGroup'

    __table_args__ = {}

    #column definitions
    id = Column(u'id', INTEGER(), primary_key=True, nullable=False)
    name = Column(u'name', INTEGER())

    #relation definitions
    Permissions = relation('Permission', primaryjoin='TgRoup.id==permissionGroup.c.group_id', secondary=permissionGroup, secondaryjoin='permissionGroup.c.permission_id==Permission.id')
    Users = relation('User', primaryjoin='TgRoup.id==userGroup.c.group_id', secondary=userGroup, secondaryjoin='userGroup.c.user_id==User.id')

from datetime import datetime

class User(DeclarativeBase):
    __tablename__ = 'User'

    __table_args__ = {}

    #column definitions
    accept = Column(u'accept', INTEGER())
    email = Column(u'email', VARCHAR(length=254))
    id = Column(u'id', INTEGER(), primary_key=True, nullable=False)
    nickname = Column(u'nickname', VARCHAR(length=254))
    password = Column(u'password', VARCHAR(length=254))
    reg_time = Column(u'reg_time', DATETIME())
    submit = Column(u'submit', INTEGER())
    username = Column(u'username', VARCHAR(length=254))
    is_active = Column(u'is_active', BOOLEAN, default=True, nullable=False)
    last_login = Column(u'last_login', DATETIME(), default=datetime.now(), nullable=False)

    #relation definitions
    TGroups = relation('TgRoup', primaryjoin='User.id==userGroup.c.user_id', secondary=userGroup, secondaryjoin='userGroup.c.group_id==TgRoup.id')

    def is_anonymous(self):
        """
        Always returns False. This is a way of comparing User objects to
        anonymous users.
        """
        return False
    
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        
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
        return check_password(raw_password, self.password, setter)

from cup_oj.auth.signals import user_logged_in
from django.utils import timezone

def update_last_login(sender, user, **kwargs):
    """
    A signal receiver which updates the last_login date for
    the user logging in.
    """
    user.last_login = timezone.now()
    session = Session()
    session.merge(user)
    session.commit()
    session.close()
user_logged_in.connect(update_last_login)

class AnonymousUser(object):
    id = None
    username = ''
    is_staff = False
    is_active = False
    is_superuser = False

    def __init__(self):
        pass

    def __unicode__(self):
        return 'AnonymousUser'

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __eq__(self, other):
        return isinstance(other, self.__class__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return 1 # instances always return the same hash value

    def save(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

    def set_password(self, raw_password):
        raise NotImplementedError

    def check_password(self, raw_password):
        raise NotImplementedError

    def _get_groups(self):
        return self._groups
    groups = property(_get_groups)

    def _get_user_permissions(self):
        return self._user_permissions
    user_permissions = property(_get_user_permissions)

    def get_group_permissions(self, obj=None):
        return set()

    def has_perms(self, perm_list, obj=None):
        for perm in perm_list:
            if not self.has_perm(perm, obj):
                return False
        return True

    def is_anonymous(self):
        return True

    def is_authenticated(self):
        return False
