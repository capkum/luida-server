# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request, jsonify
from api.database import db
from .models import Accounts
from common.crypto import passwd_crypt
from sqlalchemy.exc import IntegrityError, OperationalError
import api.status as STATUS


acnt = Blueprint('accounts', __name__)


@acnt.route('/accounts', methods=['POST', 'GET'])
def accounts():
    """ 회원가입 """
    try:
        name = request.values.get('name')
        email = request.values.get('email')
        nickname = request.values.get('nickname')
        passwd = passwd_crypt(request.values.get('passwd'))
        device_id = request.values.get('device_id')

        result = Accounts(name, email, nickname, passwd, device_id)

        db.session.add(result)
        db.session.commit()

        return jsonify(status=STATUS.SUCCESS)

    except IntegrityError:
        db.session.rollback()
        return jsonify(status=STATUS.DUPLICATE_ERR)

    except OperationalError:
        return jsonify(status=STATUS.DB_CONNECT_ERR)

    except AttributeError:
        return jsonify(status=STATUS.NONTYPE_ERR)

    except Exception:
        return jsonify(status=STATUS.ACCOUNT_ERR)


@acnt.route('/duplicate/email/<email>', methods=['GET'])
def email_duplicate_check(email):
    """ 이메일 중복 체크 """

    check = Accounts.query.filter_by(email=email)
    result = True if check is None else False
    return jsonify(duplicate=result)


@acnt.route('/duplicate/nickname/<nickname>', methods=['GET'])
def nickname_duplicate_check(nickname):
    """ 별명 중복 검사  """

    check = Accounts.query.filter_by(nickname=nickname)
    result = True if check is None else False
    return jsonify(duplicate=result)
