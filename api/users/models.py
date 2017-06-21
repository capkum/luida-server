import uuid

from api.users.base import db
from sqlalchemy.orm import class_mapper


class ToDictMixin(object):
    def to_dict(self):
        mapper = class_mapper(self.__class__)
        ret = {}
        for column in mapper.columns:
            value = getattr(self, column.name)
            if isinstance(value, uuid.UUID):
                value = str(value)
            ret[column.name] = value
        return ret


class User(db.Model, ToDictMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    passwd = db.Column(db.String(20), nullable=False)

    def __init__(self, username, email, passwd):
        self.username = username
        self.email = email
        self.passwd = passwd
