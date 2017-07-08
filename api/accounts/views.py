from flask import request, jsonify

import api.status as STATUS
import api.auth.auth_proc as auth

from .models import Accounts
from api.accounts import acnt
from api.database import db
from api.common.utils import get_account_by_email


@acnt.route('/accounts', methods=['POST'])
def accounts():
    """ 회원가입 """
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


@acnt.route('/account/emailChk/<email>', methods=['GET'])
def emailChk(email):
    """ 이메일검사 """
    account = get_account_by_email(email)
    return jsonify(account.to_dict())


@acnt.route('/account/nkChk/<nickname>', methods=['GET'])
def nkChk(nickname):
    """ 이메일검사 """
    return auth.get_account_by_nickname(nickname)


def duplicate_check():
    pass
