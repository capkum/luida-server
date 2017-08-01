# -*- coding: utf-8 -*-

import pytest  # noqa
from flask import Flask, g
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as alembicConfig
from server_api.auth.views import auth
from server_api.accounts.views import acnt
from flask_redis import FlaskRedis


@pytest.fixture(scope='session')
def create_app():
    app = Flask(__name__)
    db = SQLAlchemy()

    # setting
    app.config.from_object('luida_server.settings.TestLuidaConfig')

    db.init_app(app)
    migrate = Migrate(app, db)  # noqa

    app.register_blueprint(auth)
    app.register_blueprint(acnt)

    app_context = app.app_context()
    app_context.push()

    yield app
    app_context.pop()


@pytest.fixture(scope='session')
def db(create_app):

    app = create_app
    test_db_url = app.config['SQLALCHEMY_DATABASE_URI']
    alembic_ini = app.config['ALEMBIC_INI']

    engine = create_engine(test_db_url, echo=True)
    session = sessionmaker(bind=engine)

    _db = {'engine': engine,
           'session': session}

    with app.app_context():
        alembic_cfg = alembicConfig(alembic_ini)
        alembic_cfg.set_main_option("script_location", "migrations")
        alembic_cfg.set_main_option('sqlalchemy.url', test_db_url)
        alembic_upgrade(alembic_cfg, 'head')

    yield _db
    engine.dispose()


@pytest.fixture(scope='function')
def session(db):
    session = db['session']()
    g.db = session
    yield session
    session.rollback()
    session.close()


@pytest.fixture(scope='session')
def flask_client(create_app):
    return create_app.test_client()
