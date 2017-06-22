# -*- coding: utf-8 -*-

from flask import Blueprint, request
from flask import jsonify
from api.users.models import Users
from api.users.models import db
from api.users import passwd_crypt
from settings import SECURET_KEY, JWT_EXPIRE

import datetime
import jwt


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    email = request.values.get('email')
    passwd = passwd_crypt(request.values.get('passwd'))

    try:
        result = Users.query.filter_by(email=email, passwd=passwd).first()

        # 로그인 결과
        if type(result) is 'NoneType':
            return 'login fail'

        current_time = datetime.datetime.utcnow()

        # 데이터부의 암호화가 필요함
        create_token = jwt.encode(
            {
                'email': result.email,
                'id': result.id,
                'exp': current_time + datetime.timedelta(seconds=JWT_EXPIRE)
            },
            SECURET_KEY,
            algorithm='HS256')

        json_data = jsonify(
            email=result.email,
            username=result.username,
            status='login success'
        )

        json_data.headers.add('token', create_token)

        return json_data

    except Exception as e:
        print(str(e))
        return 'login fail'


@auth.route('/signout', methods=['DELETE'])
def signout():
    try:
        _email = request.values.get('email')
        _passwd = request.values.get('passwd')

        user_token = request.headers.get('token')
        userid = jwt.decode(user_token, SECURET_KEY, algorithm='HS256')

        user = Users.query.filter_by(id=userid['id'], passwd=_passwd).first()

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
