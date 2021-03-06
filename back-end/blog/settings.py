import os
import sys



class BaseConfig:
    JSON_AS_ASCII = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/test'


class ProductionConfig(BaseConfig):
    pass


class DevConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True


config = {
    'development': DevConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
