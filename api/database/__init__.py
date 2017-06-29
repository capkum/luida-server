# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import class_mapper
from flask_redis import FlaskRedis
import uuid

db = SQLAlchemy()
# redis
redis_db = FlaskRedis()


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
