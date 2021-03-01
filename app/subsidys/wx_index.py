from flask import Blueprint, jsonify, request
from app.models import Service
import requests
from app.config import small, city_code
from app.models import Service, Advertising

wxIndex = Blueprint('wxIndex', __name__)


@wxIndex.route('/index/')
def index():
    code = request.args.get('code')
    openid = request.args.get('openid')

    if openid:
        pass
    # 定义首页返回数据
    indexdata = {}
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
