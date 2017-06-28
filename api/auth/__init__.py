# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request, jsonify
from api.account.models import Accounts
from api.database import db
from common.crypto import passwd_crypt, token_generator
import jwt
import settings
import sqlalchemy.exc

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    """ 로그인 """
    _email = request.values.get('email')
    _passwd = passwd_crypt(request.values.get('passwd'))

    try:
        result = Accounts.query.filter_by(email=_email, passwd=_passwd).first()
        # a = db.session.query(Accounts.email).filter(Accounts.email == _email)
        # print(db.session.query(a.exists()).scalar())

        # 로그인 결과
        if result is None:
            return jsonify(status=settings.EMAIL_PW_ERR)

        # 토큰 생성
        create_token = token_generator()

        # return data
        json_data = jsonify(
            status=settings.SUCCESS,
            userid=result.seq
        )
        json_data.headers.add('token', create_token)

        return json_data

    except sqlalchemy.exc.OperationalError as e:
        return jsonify(status=settings.DB_CONNECT_ERR)

    except Exception as e:
        print(str(e))
        return jsonify(status=settings.EMAIL_PW_ERR)


@auth.route('/signout', methods=['DELETE'])
def signout():
    """
    회원 탈퇴
    ToDo
    1. 탈퇴시 업로드어있던 파일을들 삭제
    2. 거래정보는 삭제하면 안된다
    3. 토큰 유효성 검사후 토큰 정보로 삭제
    """
    try:
        _email = request.values.get('email')
        _passwd = request.values.get('passwd')

        user_token = request.headers.get('token')
        userid = jwt.decode(
            user_token, settings.SECURET_KEY, algorithm='HS256')

        user = Accounts.query.filter_by(
            id=userid['id'], passwd=_passwd).first()

        if type(user) is not 'NoneType':
            db.session.delete(user)
            db.session.commit()

            rt = jsonify(email=_email, passwd=_passwd,
                         status='delete success')
            return rt

    except jwt.ExpiredSignatureError as e:
        print(str(e))
        return jsonify({'status': '토큰 기간 만료'})

    except Exception as e:
        print(str(e))
        return 'delete fail'
