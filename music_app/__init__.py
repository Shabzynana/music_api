import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


app.config['SECRET_KEY'] = 'mysegc***'

########################   ####################

        # SQL DATABASE AND MODELS

##########################################
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_pre_ping": True}
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://shabzy:1111@localhost:5432/music"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db,render_as_batch=True)

bcrypt = Bcrypt(app)


ma = Marshmallow(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'



mail = Mail(app)


from music_app.users.views import users

app.register_blueprint(users)
