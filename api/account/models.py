# -*- coding: utf-8 -*-

from api.database import ToDictMixin
from api.database import db
from common.util import creat_timestamp


class Accounts(db.Model, ToDictMixin):
    seq = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(12), nullable=False, doc='이름')
    email = db.Column(db.String(120), unique=True, nullable=False, doc='email')
    nickname = db.Column(db.String(20), unique=True,  nullable=False, doc='별명')
    passwd = db.Column(db.String(64), nullable=False, doc='비밀번호')
    device_id = db.Column(db.String(200), doc='안드로이드 아이디')
    crated_at = db.Column(db.DateTime, nullable=False, doc='작성일')

    def __init__(self, name, nickname, passwd, device_id, crated_at):
        self.name = name
        self.nickname = nickname
        self.passwd = passwd
        self.device_id = device_id
        self.crated_at = creat_timestamp()
