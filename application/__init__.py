import os
# import Flask class from the flask module
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask import Flask
 # create a new instance of Flask and store it in app 
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
app.config['SECRET_KEY'] = str(os.getenv('SECRET_KEY'))
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
 # import the ./application/routes.py file
from application import routes
