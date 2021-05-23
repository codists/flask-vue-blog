from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from .extensions import db  


class User(db.Model):
    """
    用户模型
    """
    id = db.Column(db.Integer, primary_key=True)
    telephone = db.Column(db.String(11), nullable=False, unique=True)
    nickname = db.Column(db.String(24), nullable=False)
    avatar = db.Column(db.String(100))
    _password = db.Column('password', db.String(128), nullable=False)

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)
    
    def check_password(self, value):
        return check_password_hash(self._password, value)


class Article(db.Model):
    """
    文章模型
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    publish_time = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='articles')
