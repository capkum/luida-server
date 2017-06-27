# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request, jsonify
from api.database import db
from .models import Accounts
from common.crypto import passwd_crypt
from sqlalchemy.exc import IntegrityError
import settings
import pymysql.err

acnt = Blueprint('account', __name__)


@acnt.route('/account', methods=['POST', 'GET'])
def account():
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

        return jsonify(status=settings.SUCCESS)

    except IntegrityError as e:
        print(str(e))
        db.session.rollback()
        return jsonify(status=settings.DUPLICATE_ERR)

    except pymysql.err.OperationalError as e:
        print(str(e))
        return jsonify(status=settings.NONTYPE_ERR)

    except AttributeError:
        return jsonify(status=settings.NONTYPE_ERR)

    except Exception as e:
        print(str(e))
        return jsonify(status=settings.ACCOUNT_ERR)


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
