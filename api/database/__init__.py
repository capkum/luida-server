# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import class_mapper
import uuid

db = SQLAlchemy()


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
