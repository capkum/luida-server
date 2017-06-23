# -*- coding: utf-8 -*-
from api.database import ToDictMixin
from api.database import db


class Users(db.Model, ToDictMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    passwd = db.Column(db.String(64), nullable=False)

    def __init__(self, username, email, passwd):
        self.username = username
        self.email = email
        self.passwd = passwd
