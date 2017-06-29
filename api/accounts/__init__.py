# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import request, jsonify
from api.database import db
from .models import Accounts
import api.status as STATUS


acnt = Blueprint('accounts', __name__)


@acnt.route('/accounts', methods=['POST', 'GET'])
def accounts():
    """ 회원가입 """
    if request.method == 'POST':
        name = request.values.get('name')
        email = request.values.get('email')
        nickname = request.values.get('nickname')
        passwd = request.values.get('passwd')
        device_id = request.values.get('device_id')

        result = Accounts(name, email, nickname, passwd, device_id)
        db.session.add(result)
        db.session.commit()
        return jsonify(status=STATUS.SUCCESS)

    result = [account.to_dict() for account in Accounts.query.all()]
    return jsonify(accounts=result)


@acnt.route('/duplicate/email/<email>', methods=['GET'])
def email_duplicate_check(email):
    """ 이메일 중복 체크 """
    result = Accounts.query.filter_by(email=email).first()
    return jsonify(duplicate=bool(result))


@acnt.route('/duplicate/nickname/<nickname>', methods=['GET'])
def nickname_duplicate_check(nickname):
    """ 별명 중복 검사  """
    result = Accounts.query.filter_by(nickname=nickname).first()
    return jsonify(duplicate=bool(result))
