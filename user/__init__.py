from user.models import User
from user.models import db
from flask import Blueprint
from flask import request, jsonify
import jwt

users = Blueprint('user', __name__)
secret_key = 'hubmedia'


@users.route('/signup', methods=['POST'])
def create():
    try:
        _username = request.values.get('username')
        _email = request.values.get('email')
        _passwd = request.values.get('passwd')

        createUser = User(_username, _email, _passwd)
        db.session.add(createUser)
        db.session.commit()

        rt = jsonify(username=_username,
                     email=_email, passwd=_passwd,
                     status='success')
        return rt

    except Exception as e:
        print(str(e))
        return 'false'


@users.route('/login', methods=['POST'])
def login():
    _email = request.values.get('email')
    _passwd = request.values.get('passwd')

    try:
        result = User.query.filter_by(email=_email, passwd=_passwd).first()

        # 로그인 결과
        if type(result) is 'NoneType':
            return 'login fail'

        create_token = jwt.encode(
            {
                'email': result.email,
                'id': result.id
            }, secret_key, algorithm='HS256')

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


@users.route('/logout')
def logout():
    return 'logout'


@users.route('/signout', methods=['DELETE'])
def signout():
    try:
        _email = request.values.get('email')
        _passwd = request.values.get('passwd')

        user_token = request.headers.get('token')
        userid = jwt.decode(user_token, secret_key, algorithm='HS256')

        user = User.query.filter_by(id=userid['id'], passwd=_passwd).first()

        if type(user) is not 'NoneType':
            db.session.delete(user)
            db.session.commit()

            rt = jsonify(email=_email, passwd=_passwd,
                         status='delete success')
            return rt

    except Exception as e:
        print(str(e))
        return 'delete fail'
