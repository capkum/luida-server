# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request, jsonify
from .models import Accounts
from api.database import db

acnt = Blueprint('account', __name__)


@acnt.route('/account', methods=['POST'])
def account():

    try:
        name = request.values.get('name')
        email = request.values.get('email')
        nickname = request.values.get('email')
        passwd = request.values.get('passwd')
        device_id = request.values.get('device_id')

        result = Accounts(name, email, nickname, passwd, device_id)

        db.session.add(result)
        db.session.commit()

        return jsonify(status=200)

    except Exception as e:
        print(str(e))
        return jsonify(status=4001)
