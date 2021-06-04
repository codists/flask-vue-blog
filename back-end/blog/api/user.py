# @Date  : 2021/6/4
# @Author: Hugh
# @Email : 609799548@qq.com

from datetime import datetime

from flask import request, Blueprint

from ..models import User
from ..extensions import db
from ..utils import generate_jwt

bp = Blueprint('user', __name__, url_prefix='/api/v1/user/')


@bp.post('register')
def register():
    request_data = request.json or {}
    request_telephone = request_data.get('telephone')
    request_password = request_data.get('password')
    request_nickname = request_data.get('nickname')

    if request_nickname and request_telephone and request_password:
        if User.find_by_telephone(request_telephone):
            return {'code': 400, 'msg': 'user already exists'}
        user = User(telephone=request_telephone, password=request_password, nickname=request_nickname)
        db.session.add(user)
        db.session.commit()
        return {'code': 200, 'msg': 'success'}
    else:
        return {'code': 400, 'msg': 'missing parameter'}


@bp.post('login')
def login():
    request_data = request.json or {}
    request_telephone = request_data.get('telephone')
    request_password = request_data.get('password')
    if request_telephone and request_password:
        user = User.find_by_telephone(request_telephone)
        if not user or not (user.check_password(request_password)):
            return {'code': 400, 'msg': 'telephone or password error'}
        return {'code': 200, 'msg': 'success', 'token': generate_jwt({'user_id': user.id})}
    return {'code': 400, 'msg': 'missing parameter'}

