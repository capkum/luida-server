# -*- coding: utf-8 -*-

from flask import request
from server_api.database import db
from .models import Accounts
import luida_server.status as STATUS
from server_api.common.util import lr_trim


def registe_account():
    name = lr_trim(request.values.get('name'))
    email = lr_trim(request.values.get('email'))
    nickname = lr_trim(request.values.get('nickname'))
    passwd = lr_trim(request.values.get('passwd'))
    device_id = lr_trim(request.values.get('device_id'))

    result = Accounts(name, email, nickname, passwd, device_id)
    db.session.add(result)
    db.session.commit()

    return STATUS.SUCCESS
