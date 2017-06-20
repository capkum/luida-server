from user.models import User
from user.models import db
from flask import Blueprint
from flask import request

users = Blueprint('user', __name__)


@users.route('/signup', methods=['POST'])
def create():
    try:
        _username = request.values.get('username')
        _email = request.values.get('email')
        _passwd = request.values.get('passwd')

        createUser = User(_username, _email, _passwd)
        db.session.add(createUser)
        db.session.commit()
        return 'success'

    except Exception as e:
        return 'false'


@users.route('/login', methods=['POST'])
def login():
    _email = request.values.get('email')
    _passwd = request.values.get('passwd')

    try:
        result = User.query.filter_by(email=_email, passwd=_passwd).all()

        # 로그인 결과
        if len(result) <= 0:
            return 'login fail'

        return 'login success'

    except Exception:
        return 'login fail'


@users.route('/logout')
def logout():
    return 'logout'


@users.route('/signout', methods=['DELETE'])
def signout():
    try:
        _email = request.values.get('email')
        _passwd = request.values.get('passwd')
        user = User.query.filter_by(email=_email, passwd=_passwd).first()

        if len(user) > 0:
            db.session.delete(user)
            db.session.commit()
            return 'delete success'

    except Exception as e:
        return 'delete fail'
