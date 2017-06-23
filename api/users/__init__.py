# -*- coding: utf-8 -*-

from flask import Blueprint
from api.users.models import Users
from api.database import db
from flask import request, jsonify
from common.crypto import passwd_crypt

users = Blueprint('users', __name__)


@users.route('/signup', methods=['POST'])
def create():
    try:
        _username = request.values.get('username')
        _email = request.values.get('email')
        _passwd = request.values.get('passwd')

        createUser = Users(_username, _email, passwd_crypt(_passwd))
        db.session.add(createUser)
        db.session.commit()

        rt = jsonify(username=_username,
                     email=_email, passwd=_passwd,
                     status='success')
        return rt

    except Exception as e:
        print(str(e))
        return '회원가입 실패'
