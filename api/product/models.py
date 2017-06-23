# -*- coding: utf-8 -*-
from api.database import db
from api.database import ToDictMixin


class Products(db.Model, ToDictMixin):
    filename = db.Column(db.String(120))

    def __init__(self, filename):
        self.filename = filename
