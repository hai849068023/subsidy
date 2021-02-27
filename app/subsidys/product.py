from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models import Service
from app import db
from flask_login import login_required

product = Blueprint('product', __name__)


@product.route('/product/')
# @login_required
def products():
    return render_template('product.html')


@product.route('/service/')
# @login_required
def serviceList():
    serdata = Service.query.all()
    data = {}
    for ser in serdata:
        data[ser.id] = [ser.id, ser.service_name, ser.describe]
    return jsonify(data)


# 添加服务分类
@product.route('/service/add/', methods=['GET', 'POST'])
# @login_required
def serviceList_add():
    if request.method == 'GET':
        return render_template('service_add.html')
    service_name = request.form['service_name']
    describe = request.form['describe']
    introduce = request.form['introduce']
    if service_name and describe and introduce:
        service = Service(service_name=service_name, describe=describe, introduce=introduce)
        db.session.add(service)
        db.session.commit()
        return render_template(url_for('.serviceList'), success='操作成功！')
    return '有必传项未提供'


# 编辑服务分类
@product.route('/service/edit/<id>/', methods=['GET', 'POST'])
# @login_required
def serviceList_edit(id):
    service = Service.query.get(id)
    if request.method == 'GET':
        return render_template('service_add.html', serviceData=service)
    service.service_name = request.form['service_name']
    service.describe = request.form['describe']
    service.introduce = request.form['introduce']
    db.session.commit()
    return '修改成功'