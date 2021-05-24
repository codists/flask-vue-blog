import io

from flask import request, make_response, Blueprint

from blog.utils.captcha import generate_random, Captcha

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
    random_number = generate_random()
    image = captcha.generate_graph_captcha(random_number)
    out = io.BytesIO()
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp

