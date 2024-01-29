import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from music_app.config import App_Config


cors = CORS()

db = SQLAlchemy()

bcrypt = Bcrypt()

ma = Marshmallow()

login_manager = LoginManager()

# sess = Session()

mail = Mail()

def create_app():
    """
    Create a new instance of the app with the given configuration.

    :param config_class: configuration class
    :return: app
    """
    # Initialize Flask-

    app = Flask(__name__)
    app.config.from_object(App_Config)

    # Initialize SQLAlchemy
    db.init_app(app)

   #   initialise seesion
   #   sess.init_app(app)

    #  Initialize login manager
    login_manager.init_app(app)
    login_manager.login_view = 'users.login' 

    # Initialize Bcrypt
    bcrypt.init_app(app)

    # Initialize Bcrypt
    mail.init_app(app)

    ma.init_app(app)

    # Importing the models here so it can create the empty tables.
    # the routes

    from music_app.users.views import users

    app.register_blueprint(users)

    # create db tables from models if not exists
    with app.app_context():
        db.create_all()

    return app