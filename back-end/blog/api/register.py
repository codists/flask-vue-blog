from flask import request, Blueprint

bp = Blueprint('register', __name__, url_prefix='/')


@bp.route('/register')
def register():
    request_data = request.json
    request_telephone = request_data.get('telephone')
    request_sms_code = request.get('sms_code')
    request_password = request.get('password')
    request_nickname = request.get('nickname')


@bp.get('/graph_captcha')
def graph_captcha():
    pass


