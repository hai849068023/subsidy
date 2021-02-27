from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import pymysql
pymysql.install_as_MySQLdb()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/subsidy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'just a program'
db = SQLAlchemy(app)
login_manager = LoginManager(app)


from app.subsidys.admin import admin
from app.subsidys.product import product
app.register_blueprint(admin)
app.register_blueprint(product)


@login_manager.user_loader
def load_user(userid):
    from app.models import Users
    user = Users.query.get(userid)
    return user

login_manager.login_view ='admin.login'