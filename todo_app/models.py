from todo_app import db,app,login_manager
from flask_login import UserMixin
# from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    profile_image = db.Column(db.String(64),nullable=False,default='default_profile.png')
    email = db.Column(db.String(64),unique=True,index=True)
    first_name = db.Column(db.String(64),unique=False,index=True)
    last_name = db.Column(db.String(64),unique=False,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    gender = db.Column(db.String(10))
    password = db.Column(db.String(128))

    # def __init__(self,email,first_name,last_name,username,gender,password):
    def __init__(self,first_name,last_name,username,email,gender,password):

        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.gender = gender
        self.password = password


    def __repr__(self):
        return f" Username: {self.username}"
