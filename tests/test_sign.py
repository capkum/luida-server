# -*- coding: utf-8 -*

import pytest
from server_api.accounts.models import Accounts


@pytest.fixture(scope='function')
def accounts(session):
    name = '김성진'
    email = 'test@test.com'
    nickname = 'tester'
    passwd = 'furumee#1'
    device_id = 'testDevice'
    result = Accounts(name, email, nickname, passwd, device_id)
    session.add(result)
    print(session.new)
    print(session.dirty)
    return result


def test_signin(flask_client, accounts):
    data = {
        'email': 'test@test.com',
        'passwd': 'furumee#1'
    }

    resp = flask_client.post('/login', data=data)
    print(resp.status_code)
    assert resp.status_code == 200
