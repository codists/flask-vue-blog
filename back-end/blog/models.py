from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from .extensions import db  


class User(db.Model):
    """
    用户模型
    """
    id = db.Column(db.Integer, primary_key=True)
    telephone = db.Column(db.String(11), nullable=False, unique=True)
    nickname = db.Column(db.String(24), nullable=False, unique=True)
    avatar = db.Column(db.String(100))
    _password = db.Column('password', db.String(128), nullable=False)

    articles = db.relationship('Article', backref='user')

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)
    
    def check_password(self, value):
        return check_password_hash(self.password, value)

    @classmethod
    def find_by_telephone(cls, telephone):
        return cls.query.filter_by(telephone=telephone).first()


class Article(db.Model):
    """
    文章模型
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    publish_time = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

