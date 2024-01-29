from music_app import db,login_manager
from music_app.config import App_Config

from itsdangerous import URLSafeTimedSerializer
from music_app.models import User


def get_token(self):
    s = URLSafeTimedSerializer(App_Config['SECRET_KEY'])
    return s.dumps({'user_id': self.id})
# @staticmethod
def verify_token(token, expires_sec=180):
    s = URLSafeTimedSerializer(App_Config['SECRET_KEY'])
    try:
        user_id = s.loads(token, max_age=expires_sec)['user_id']
    except Exception:
        return None
    return User.query.get(user_id)
