# -*- coding: utf-8 -*-

from flask import Flask
from server_api.database import db, redis_db
from server_api.accounts.views import acnt
from server_api.auth.views import auth
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('luida_server.settings.DevelopmentConfig')

# mariaDB, Redis
db.init_app(app)
redis_db.init_app(app)
migrate = Migrate(app, db)

# blueprint
app.register_blueprint(acnt)
app.register_blueprint(auth)

# error handler
from luida_server.error_handler import * # noqa


if __name__ == '__main__':
    app.run()
