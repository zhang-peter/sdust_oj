from cup_oj.auth.models import User
from cup_oj.sa_conn import Session

from cup_oj.auth.hashers import make_password

class SABackend(object):
    """
    Authenticates against cup_oj.models.User.
    """
    
    supports_inactive_user = True

    # TODO: Model, login attribute name and password attribute name should be
    # configurable.
    def authenticate(self, username=None, password=None):
        session = Session()
        user = session.query(User).filter_by(username=username).first()
        
        if user is not None:
            if not user.check_password(password):
                user = None     

        session.close()
        return user

    def get_user(self, user_id):
        session = Session()
        user = session.query(User).get(user_id)
        session.close()
        return user 