# -*- coding: utf-8 -*-

from server_api.accounts.models import Accounts
from server_api.common.crypto import token_generator
from server_api.database import redis_db
import luida_server.status as STATUS


class AuthDao(object):

    def __init__(self, email):
        self.email = email
        # self.user = self.user(email)

    def user(self):
        rt = Accounts.query.filter_by(email=self.email).first_or_404()

        return rt.to_dict()

    def create_redis_data(self):
        from main import app

        # create token
        create_token = token_generator()

        # register token in redis
        redis_db.delete(self.email)
        redis_db.set(self.email, create_token)
        redis_db.expire(self.email, app.config['REDIS_EXPIRE'])

        return {'status_code': STATUS.SUCCESS, 'token': create_token}

    def delete_redis_data(self):
        redis_db.delete(self.email)

        return {'status_code': STATUS.SUCCESS}
