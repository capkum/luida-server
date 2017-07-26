# -*- coding: utf-8 -*-

from main import app


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    response.headers.add('Access-Control-Expose-Headers', 'autho_tk')
    return response

