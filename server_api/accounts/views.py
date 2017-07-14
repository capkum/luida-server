# -*- coding: utf-8 -*-

from flask import request, jsonify
from server_api.accounts import acnt
from server_api.database import db
from .models import Accounts
import luida_server.status as STATUS


@acnt.route('/account', methods=['POST'])
def reg_account():

    name = request.values.get('name')
    email = request.values.get('email')
    nickname = request.values.get('nickname')
    passwd = request.values.get('passwd')
    device_id = request.values.get('device_id')

    result = Accounts(name, email, nickname, passwd, device_id)
    db.session.add(result)
    db.session.commit()

    return jsonify(status=STATUS.SUCCESS)
