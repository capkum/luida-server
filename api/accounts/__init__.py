# -*- coding: utf-8 -*-
from flask import Blueprint
from api.accounts.registe_proc import register

acnt = Blueprint('accounts', __name__)


@acnt.route('/accounts', methods=['POST'])
def accounts():
    """ 회원가입 """
    return register()


# @acnt.route('/duplicate/email/<email>', methods=['GET'])
# def email_duplicate_check(email):
#     """ 이메일 중복 체크 """
#     result = Accounts.query.filter_by(email=email).first()
#     return jsonify(duplicate=bool(result))


# @acnt.route('/duplicate/nickname/<nickname>', methods=['GET'])
# def nickname_duplicate_check(nickname):
#     """ 별명 중복 검사  """
#     result = Accounts.query.filter_by(nickname=nickname).first()
#     return jsonify(duplicate=bool(result))
