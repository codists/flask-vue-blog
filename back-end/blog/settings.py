import os
import sys

WIN = sys.platform.startswith('win')
prefix = '///' if WIN else '////'


class BaseConfig:
    JSON_AS_ASCII = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:' + prefix + os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data.db')


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
