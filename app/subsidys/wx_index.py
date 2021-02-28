from flask import Blueprint, jsonify
from app.models import Service
import requests
from app.config import small, city_code
from app.models import Service, Advertising

wxIndex = Blueprint('wxIndex', __name__)


@wxIndex.route('/index/')
def index():
    # wx_login = requests.get(
    #     'https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code=JSCODE&grant_type=authorization_code'.format(
    #         small['appid'], small['appsecret']))
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
    # 加入车型数据
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
