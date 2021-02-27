from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    real_name = db.Column(db.String(28))
    nick_name = db.Column(db.String(28))
    tel = db.Column(db.String(11))
    head_img = db.Column(db.String(128))
    password = db.Column(db.String(128))
    is_admin = db.Column(db.String(5))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password, password)


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(28), comment='服务名称')
    describe = db.Column(db.String(128))


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(28), comment='产品名称')
    p_img = db.Column(db.String(128))
    describe = db.Column(db.String(128), comment='描述')
    price = db.Column(db.String(28))
    inventory = db.Column(db.Integer(), comment='库存')
    product_group = db.relationship('Product_group', backref='person', lazy='dynamic')


class Product_group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(28), comment='分类名称')
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))