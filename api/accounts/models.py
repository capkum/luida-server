# -*- coding: utf-8 -*-

from api.database import ToDictMixin
from api.database import db
import datetime


class TimestampMxin(object):
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())


class Accounts(db.Model, ToDictMixin, TimestampMxin):
    seq = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(12), nullable=False, doc='이름')
    email = db.Column(db.String(120), unique=True, nullable=False, doc='email')
    nickname = db.Column(db.String(20), unique=True, nullable=False, doc='별명')
    passwd = db.Column(db.String(64), nullable=False, doc='비밀번호')
    profile_img = db.Column(db.String(255), nullable=True, doc='프로필 사진')
    voice = db.Column(db.String(120), nullable=True, doc='목소리')
    point = db.Column(db.Integer, default=0, nullable=True, doc='포인트')
    evnt_point = db.Column(db.Integer, default=0, nullable=True, doc='이벤트포인트')
    device_id = db.Column(db.String(200), doc='안드로이드 아이디')

    def __init__(self, name, email, nickname, passwd, device_id,
                 profile_img=None, voice=None, point=0, evnt_point=0):
        self.name = name
        self.email = email
        self.nickname = nickname
        self.passwd = passwd
        self.device_id = device_id
        self.profile_img = profile_img
        self.voice = voice
        self.point = point
        self.evnt_point = evnt_point
