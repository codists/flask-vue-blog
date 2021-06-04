from pathlib import Path
from datetime import datetime

import jwt
from flask import current_app


BASEDIR = Path(__file__).parent.parent.parent


def generate_jwt(payload, expiry=None, secret=None):
    """
    生成jwt
    :param payload: dict 载荷
    :param expiry: datetime 有效期
    :param secret: 密钥
    :return: jwt
    """
    if not expiry:
        expiry = datetime.now().timestamp() + 60 * 60 * 24

    _payload = {'exp': expiry}
    _payload.update(payload)
    if not secret:
        secret = current_app.config['JWT_SECRET']
    return jwt.encode(_payload, secret, algorithm='HS256')


def verify_jwt(token, secret=None):
    """
    检验jwt
    :param token: jwt
    :param secret: 密钥
    :return: dict: payload
    """
    if not secret:
        secret = current_app.config['JWT_SECRET']
    try:
        payload = jwt.encode(token, secret, algorithm=['HS256'])
    except jwt.PyJWTError:
        payload = None
    return payload
