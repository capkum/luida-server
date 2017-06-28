# -*- coding: utf-8 -*-
import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

DB_URI = 'mysql+pymysql://luida:luida123@localhost/luida?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = DB_URI
MAX_CONTENT_LENGTH = 1024 * 1024 * 16
UPLOAD_FOLDER = os.path.join(ROOT_PATH, 'upload')
CRYPTO_KEY = '62d6b80a-2d65-4d42-aa72-740b1368d0c0'
SECURET_KEY = 'hubmedia'
JWT_EXPIRE = 30


# ToDo
# 상태코드를 따로 작성해야됨
# 지금은 일단 이대로

# 상태코드
SUCCESS = 200
DB_CONNECT_ERR = 2000

# 로그인 에러
LOGIN_ERR = 4000
EMAIL_PW_ERR = 4001

# 회원가입 에러
ACCOUNT_ERR = 4100
DUPLICATE_ERR = 4101
NONTYPE_ERR = 4102


# 토큰 에러
TOOKEN_ERR = 3000
# 토큰 유효기간 에러
EXPIRE_SIGNATURE_ERR = 3001

# 인증 사진 업로드 사이즈 에러
IMG_SIZE_ERR = 5000
