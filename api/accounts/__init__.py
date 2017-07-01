# -*- coding: utf-8 -*-
from flask import Blueprint

from api.accounts.registe_proc import register
import api.auth.auth_proc

acnt = Blueprint('accounts', __name__)


@acnt.route('/accounts', methods=['POST'])
def accounts():
    """ 회원가입 """
    return register()


@acnt.route('/account/emailChk/<email>', methods=['GET'])
def emailChk(email):
    """ 이메일검사 """
    return api.auth.auth_proc.get_account_by_email(email, 'check')


@acnt.route('/account/nkChk/<nickname>', methods=['GET'])
def nkChk(nickname):
    """ 이메일검사 """
    return api.auth.auth_proc.get_account_by_nickname(nickname)
