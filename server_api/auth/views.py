# -*- coding: utf-8 -*-

from flask import request, jsonify
from werkzeug.security import check_password_hash
from .import auth
from server_api.auth.auth_dao import AuthDao
import luida_server.status as STATUS


@auth.route('/login', methods=['POST'])
def login():
    email = request.values.get('email')
    passwd = request.values.get('passwd')

    auth_dao = AuthDao(email)

    if check_password_hash(auth_dao.user()['passwd'], passwd):
        res_data = auth_dao.create_redis_data()

        resp = jsonify(
            status=res_data['status_code'],
            uid=auth_dao.user()['seq'],
            nickName=auth_dao.user()['nickname']
        )
        resp.headers['autho_tk'] = res_data['token']

        return resp

    else:
        auth_dao.delete_redis_data()
        return jsonify(status=STATUS.EMAIL_PW_ERR)
