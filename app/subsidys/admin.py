from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Users
from flask_login import login_user, current_user, logout_user, login_required

admin = Blueprint('admin', __name__)


@admin.route('/admin/')
def home():
    return render_template('admin.html')


@admin.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('.home'))

    if request.method == 'GET':
        return render_template('login.html')

    user = Users.query.filter(Users.is_admin == 1).one()
    tel = request.form['tel']
    pwd = request.form['pwd']
    if tel == user.tel and user.validate_password(pwd):
        login_user(user)
        return redirect(url_for('.home'))
    else:
        return render_template('login.html', error='账号或者密码错误')


@admin.route('/logout/')
@login_required
def logout():
    logout_user()
    return render_template('login.html')