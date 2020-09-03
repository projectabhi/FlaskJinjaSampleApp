from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '074abed1744cefd205efa25e5024bdee'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # To tell where login view is located /account url
login_manager.login_message = 'Please login to view the page'
login_manager.login_message_category = 'info'

from flaskjinjasample import routes
