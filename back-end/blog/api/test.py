from flask import Blueprint

bp = Blueprint('test', __name__, url_prefix='/')


@bp.route('')
def index():
    return {'code': 0, 'msg': 'test success.'}
