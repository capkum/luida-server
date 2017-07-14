# -*- coding: utf-8 -*-

import os


class Config(object):
    ''' default '''
    DEBUG = False
    TESTING = False
    DATABASE_URL = ''

    # app root path
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

    # mariaDB
    DB_URI = 'mysql+pymysql://luida:luida123@localhost/luida?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = DB_URI

    # securety
    CRYPTO_KEY = '62d6b80a-2d65-4d42-aa72-740b1368d0c0'
    SECRET_KEY = '\x85=\n\xc8];\xacP\xe5\xbf%\x169O\x8c+\xabS\xbeE'

    # file upload folder
    MAX_CONTENT_LENGTH = 1024 * 1024 * 16
    UPLOAD_FOLDER = os.path.join(ROOT_PATH, 'upload')

    # Redis
    REDIS_URL = "redis://localhost:6379/0"
    REDIS_EXPIRE = 20


class DevelopmentConfig(Config):
    DEBUG = True
    SERVER_NAME = '127.0.0.1:5000'


class QaConfig(Config):
    pass


class ProductConfig(Config):
    pass
