from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# 用户表
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    tel = db.Column(db.String(11))
    head_img = db.Column(db.String(128))
    password = db.Column(db.String(128))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password, password)


# 服务分组表
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(28), comment='服务名称')
    describe = db.Column(db.String(128))


# 商品分类表
class Product_group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(28), comment='分类名称')
    products = db.relationship('Product', backref='product_group', lazy='dynamic')


# 商品表
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('product_group.id'), comment='分类id')
    name = db.Column(db.String(28), comment='产品名称')
    p_img = db.Column(db.String(128))
    describe = db.Column(db.String(128), comment='描述')
    price = db.Column(db.String(28))
    inventory = db.Column(db.Integer(), comment='库存')
    shelves = db.Column(db.Integer(), comment='是否上架，1上架 0下架')
    product_group_id = db.Column(db.Integer, db.ForeignKey('Product_group.id'))


# 订单表
class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(50), comment='订单id')


# 门店表
class Stores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), comment='门店名称')
    address = db.Column(db.String(255), comment='门店详细地址')
    province = db.Column(db.String(20), comment='省份')
    city = db.Column(db.String(20), comment='市')
    area = db.Column(db.String(20), comment='区')
    phone = db.Column(db.String(20), comment='门店电话')
    work_time = db.Column(db.String(128), comment='营业时段，字符串自定义输入')
    is_open = db.Column(db.Integer(), comment='是否开启，1开启 0关闭')
    manager_openid = db.Column(db.String(128), comment='管理员openid')


# 客户表
class Customs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(50), comment='昵称')
    tel = db.Column(db.String(11), comment='手机号')
    head_img = db.Column(db.String(255), comment='头像')
    consumption = db.Column(db.Float(), comment='累计消费')
    growth_value = db.Column(db.Integer, comment='成长值')
    add_time = db.Column(db.String(50), comment='注册时间')


# 客户的汽车记录表
class Customs_cars(db.Model):
    id = db.Column(db.Integer, primary_key=True)



# 会员卡表
class Members(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String(50), comment='名称')
    need_value = db.Column(db.Integer, comment='所需成长值')


# 汽车品牌表
class Carbrand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brandname = db.Column(db.String(50), comment='品牌名称')
    type = db.Column(db.String(5), comment='字母分类')
    image = db.Column(db.String(255), comment='品牌图片')
    is_hot = db.Column(db.Integer, comment='是否热门 1热门 0默认')
    car = db.relationship('Car', backref='carbrand', lazy='dynamic')


# 汽车表
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('carbrand.id'))
    carname = db.Column(db.String(50), comment='汽车名称')
    carimg = db.Column(db.String(255), comment='汽车图片')
    carmodel = db.relationship('CarModel', backref='car', lazy='dynamic')


# 汽车型号表
class CarModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carmodel = db.Column(db.String(50), comment='汽车名称')
    years = db.Column(db.String(50), comment='年份')
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'))


# 广告表
class Advertising(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(255), comment='广告图')
    name = db.Column(db.String(255), comment='广告名称')
    is_open = db.Column(db.Integer, comment='是否开启 1开启，0关闭')
    type = db.Column(db.String(50), comment='广告类型：card套餐卡 coupons优惠券')
    cid = db.Column(db.Integer, comment='活动id')