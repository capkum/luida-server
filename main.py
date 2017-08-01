# -*- coding: utf-8 -*-

from flask import Flask
from flask_migrate import Migrate
from server_api.database import db, redis_db
from server_api.accounts.views import acnt
from server_api.auth.views import auth

app = Flask(__name__)
app.config.from_object('luida_server.settings.DevelopmentConfig')

# mariaDB, Redis, CORS
db.init_app(app)
redis_db.init_app(app)
migrate = Migrate(app, db)


# blueprint
app.register_blueprint(acnt)
app.register_blueprint(auth)

# error handler
from luida_server.error_handler import *  # noqa


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    response.headers.add('Access-Control-Expose-Headers', 'autho_tk')
    return response


if __name__ == '__main__':
    app.run()
