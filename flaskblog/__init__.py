import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt;
from flask_login import LoginManager 
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ab523826099602ab0f0b9c19b25d6278'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
# app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
print(os.environ.get('MAIL_USERNAME'),os.environ.get('MAIL_PASSWORD'))
mail = Mail(app)

from flaskblog import routes