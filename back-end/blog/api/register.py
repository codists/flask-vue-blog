import io
import string

from flask import request, make_response, Blueprint

from ..models import User
from ..extensions import db
from ..utils.cache import cache
from ..utils.captcha import generate_random_number, Captcha, SendSms

"""
1.获取图形验证码
2.验证图形验证码，发送短信验证码
3.验证短信验证码，验证用户是否已注册
"""
bp = Blueprint('register', __name__, url_prefix='/')


@bp.route('/register')
def register():
    request_data = request.json
    request_telephone = request_data.get('telephone')
    request_password = request_data.get('password')
    request_nickname = request_data.get('nickname')

    if request_nickname and request_telephone and request_password:
        if User.find_by_telephone(request_telephone):
            return {'code': 400, 'msg': 'user already exists'}
        user = User(telephone=request_telephone, password=request_password)
        db.session.add(user)
        db.session.commit()
        return {'code': 200, 'msg': 'success'}
    else:
        return {'code': 400, 'msg': 'missing parameter'}


# @bp.get('/graph_captcha')
def graph_captcha():
    """
    图形验证码
    """
    captcha = Captcha()
    random_number = generate_random_number()
    random_id = generate_random_id()
    cache.set(random_id, random_number)
    image = captcha.generate_graph_captcha(random_number)
    out = io.BytesIO()
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    resp.headers.add('random_id', random_id)
    return resp


# @bp.get('/sms_captcha')
def sms_captcha():
    """
    短信验证码
    """
    random_id = request.headers.get('random_id')
    request_graph_captcha = request.json.get('graph_captcha')
    if request_graph_captcha != cache.get(random_id):
        return {'code': 400, 'msg': 'graph captcha error'}
    telephone = request.json.get('telephone')
    if User.query.filter_by(telephone=telephone).first():
        return {'code': 400, 'msg': 'telephone already exists'}
    random_number = generate_random_number(6)
    SendSms.send(telephone, random_number)
    return {'code': 200, 'msg': 'success'}


def generate_random_id():
    source = string.digits + string.ascii_letters
    while True:
        random_id = generate_random_number(32, source)
        if cache.get(random_id) is None:
            break
    return random_id

