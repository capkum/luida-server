# -*- coding: utf-8 -*-
import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

DB_URI = 'mysql+pymysql://luida:luida123@localhost/luida?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = DB_URI
MAX_CONTENT_LENGTH = 1024 * 1024 * 16
UPLOAD_FOLDER = os.path.join(ROOT_PATH, 'upload')

SECURET_KEY = 'hubmedia'
JWT_EXPIRE = 30


# 상태코드
STATUS_SUCCESS = 200

# 로그인 에러
LOGIN_ERR = 4000
# 회원가입 에러
SIGNUP = 4001

# 토큰 에러
TOOKEN_ERROR = 3000
# 토큰 유효기간 에러
EXPIRE_SIGNATURE_ERR = 3001

# 인증 사진 업로드 사이즈 에러
IMG_SIZE_ERR = 5000
