from flask import Blueprint, jsonify, request
from app.models import Service
import requests
from app.config import small, city_code
from app.models import Service, Advertising, Customs_cars

wxIndex = Blueprint('wxIndex', __name__)


@wxIndex.route('/index/')
def index():
    code = request.args.get('code')
    openid = request.args.get('openid')
    # 定义首页返回数据
    indexdata = {}
    if openid:
        customs_car = Customs_cars.query.filter_by(openid=openid, is_used=1).first()
        if customs_car is not None:
            car_data = {'brand_img': customs_car.brand_img, 'brand': customs_car.brand, 'car': customs_car.car,
                        'model': customs_car.model, 'car_number': customs_car.car_number,
                        'last_time': customs_car.last_time, 'reg_time': customs_car.reg_time}
            indexdata['car_data'] = car_data
        else:
            return 'openid不存在'
    serData = Service.query.all()
    data = []
    for ser in serData:
        serdict = {}
        serdict['id'] = ser.id
        serdict['service_name'] = ser.service_name
        serdict['describe'] = ser.describe
        data.append(serdict)
    indexdata['service_date'] = data
    # 加入城市数据
    indexdata['city_data'] = city_code
    # 获取活动数据列表
    advs = Advertising.query.filter_by(is_open=1).all()
    adv_data = []
    for adv in advs:
        advDict = {}
        advDict['advid'] = adv.id
        advDict['advimg'] = adv.img
        adv_data.append(advDict)
    indexdata['advImg'] = adv_data
    return indexdata
