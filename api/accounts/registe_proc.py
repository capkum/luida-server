# -*- coding: utf-8 -*-

from flask import request, jsonify
from .models import Accounts
from api.database import db
import api.status as STATUS


def register():
    """ 회원 가입 """
    name = request.values.get('name')
    email = request.values.get('email')
    nickname = request.values.get('nickname')
    passwd = request.values.get('passwd')
    device_id = request.values.get('device_id')

    result = Accounts(name, email, nickname, passwd, device_id)
    db.session.add(result)
    db.session.commit()

    return jsonify(status=STATUS.SUCCESS)
    # result = [account.to_dict() for account in Accounts.query.all()]
    # return jsonify(accounts=result)


def duplicate_check():
    pass
