# -*- coding: utf-8 -*-

from flask import jsonify, request
from server_api.accounts import acnt
from server_api.common.validate import validate_param
from .account_dao import registe_account

import luida_server.status as STATUS


@acnt.route('/account', methods=['POST'])
def account():
    status_code = STATUS.SUCCESS
    
    if not validate_param('name', request.values.get('name')):
        status_code = STATUS.NAME_ERR

    elif not validate_param('email', request.values.get('email')):
        status_code = STATUS.EMAIL_ERR

    elif not validate_param('passwd', request.values.get('passwd')):
        status_code = STATUS.PASSWD_ERR

    else:
        status_code = registe_account()

    return jsonify(status=status_code)
