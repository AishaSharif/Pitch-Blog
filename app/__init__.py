from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import  UploadSet,configure_uploads,IMAGES
from flask_mail import Mail


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manger = LoginManager()
login_manger.session_protection = 'strong'
login_manger.login_view = 'auth.login'
photos = UploadSet('photos', IMAGES)
mail = Mail()


def create_app(config_name):
  app = Flask(__name__)

  # Creating app configurations
  app.config.from_object(config_options[config_name])

  # Initializing flask extensions
  bootstrap.init_app(app)
  db.init_app(app)
  login_manger.init_app(app)
  mail.init_app(app)

  # Configure UploadSet
  configure_uploads(app, photos)

  # Registering the blueprint
  from .main import main as main_blueprint
  from .auth import auth as auth_blueprint
  app.register_blueprint(main_blueprint)
  app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

  return app