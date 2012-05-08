from django.dispatch import Signal

user_logged_in = Signal(providing_args=['request', 'user'])
user_logged_out = Signal(providing_args=['request', 'user'])

from django.utils import timezone
from sdust_oj.sa_conn import Session

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