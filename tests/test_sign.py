# -*- coding: utf-8 -*

import pytest # noqa
from sqlalchemy import exc
from server_api.accounts.models import Accounts


# @pytest.fixture(scope='function')
# def accounts(session):
#     name = '김성진'
#     email = 'test@test.com'
#     nickname = 'tester'
#     passwd = 'furumee#1'
#     device_id = 'testDevice'
#     result = Accounts(name, email, nickname, passwd, device_id)
#     session.add(result)
#     return result

dumy_data = {
    'name': '김성진',
    'email': 'test@test.com',
    'nickname': 'tester',
    'passwd': 'furumee#1',
    'device_id': 'testDevice',
}


def test_signup(flask_client):

    try:
        res = flask_client.post('/account', data=dumy_data)
    except exc.IntegrityError as e:
        print(str(e.orig))
    except Exception as e:
        print(str(e.orig))
    assert res.status_code == 200


def test_signin(flask_client, create_app):
    res = flask_client.post('/login', data=dumy_data)
    assert res.status_code == 200


def test_delete_dumy_data(session):
    session.query(Accounts).delete()
    rt = session.commit()
    assert rt is None
