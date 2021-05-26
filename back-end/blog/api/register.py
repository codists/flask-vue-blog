import io
import string

from flask import request, make_response, Blueprint

from blog.models import User
from blog.utils.cache import cache
from blog.utils.captcha import generate_random_number, Captcha, SendSms

bp = Blueprint('register', __name__, url_prefix='/')


@bp.route('/register')
def register():
    request_data = request.json
    request_telephone = request_data.get('telephone')
    request_sms_code = request_data.get('sms_code')
    request_password = request_data.get('password')
    request_nickname = request_data.get('nickname')


@bp.get('/graph_captcha')
def graph_captcha():
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


@bp.get('/sms_captcha')
def sms_captcha():
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
