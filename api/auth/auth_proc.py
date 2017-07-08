# -*- coding: utf-8 -*-

from flask import request, jsonify
from werkzeug.security import check_password_hash

from api.accounts.models import Accounts
from api.database import redis_db
from common.crypto import token_generator

import api.status as STATUS
import settings as SETTINGS

from api.common.utils import get_account_by_email


def login_proc():
    "로그인"
    email = request.values.get('email')
    passwd = request.values.get('passwd')
    result = get_account_by_email(email)

    if check_password_hash(result.passwd, passwd):
        # 토큰 생성
        create_token = token_generator()

        # 토큰 redis 등록
        redis_db.delete(email)
        redis_db.set(email, create_token)
        redis_db.expire(email, SETTINGS.REDIS_EXPIRE)

        rt_data = jsonify(
            status=STATUS.SUCCESS,
            userid=result.seq,
            nickname=result.nickname,
        )
        rt_data.headers['autho_tk'] = create_token

        return rt_data

    else:
        return jsonify(status=STATUS.LOGIN_ERR)


def get_account_by_nickname(nickname):
    """ 별명 체크  """
    result = Accounts.query.filter_by(nickname=nickname).first_or_404()
    return jsonify(result.to_dict())
