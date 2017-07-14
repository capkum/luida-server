# -*- coding: utf-8 -*-


from flask import jsonify
from sqlalchemy.exc import IntegrityError, OperationalError, InternalError
from sqlalchemy.exc import DataError
from server_api.database import db
from main import app
import http
import luida_server.status as STATUS

TARGET_HTTP_ERROR_CODES = (
    http.client.BAD_REQUEST,
    http.client.UNAUTHORIZED,
    http.client.FORBIDDEN,
    http.client.NOT_FOUND,
    http.client.METHOD_NOT_ALLOWED,
    http.client.NOT_ACCEPTABLE,
    http.client.REQUEST_TIMEOUT,
    http.client.CONFLICT,
    http.client.GONE,
    http.client.LENGTH_REQUIRED,
    http.client.PRECONDITION_FAILED,
    http.client.REQUEST_ENTITY_TOO_LARGE,
    http.client.REQUEST_URI_TOO_LONG,
    http.client.UNSUPPORTED_MEDIA_TYPE,
    http.client.REQUESTED_RANGE_NOT_SATISFIABLE,
    http.client.EXPECTATION_FAILED,
    http.client.INTERNAL_SERVER_ERROR,
    http.client.NOT_IMPLEMENTED,
    http.client.BAD_GATEWAY,
    http.client.SERVICE_UNAVAILABLE,
    http.client.GATEWAY_TIMEOUT,
    http.client.HTTP_VERSION_NOT_SUPPORTED
)


def error_handler(err):
    """error to JSON format"""
    error_response = jsonify(
        code=getattr(err, 'code', http.client.INTERNAL_SERVER_ERROR),
        name=getattr(err, 'name', 'Unkonwn'),
        message=getattr(err, 'description', '')
    )

    return error_response


for error in TARGET_HTTP_ERROR_CODES:
    app.register_error_handler(error, error_handler)


@app.errorhandler(OperationalError)
def handle_db_operational_err(err):
    error_response = jsonify(
        code=STATUS.DB_OPERATION_ERR,
        name='Database operational error',
        message=str(err)
    )
    db.session.rollback()
    return error_response


@app.errorhandler(IntegrityError)
def handle_db_integrity_err(err):
    error_response = jsonify(
        code=STATUS.DUPLICATE_ERR,
        name='Database integrity error',
        # message=str(err)
    )
    db.session.rollback()
    return error_response


@app.errorhandler(AttributeError)
def handle_attribute_err(err):
    error_response = jsonify(
        code=http.client.INTERNAL_SERVER_ERROR,
        name='Attrubute error',
        message=str(err)
    )
    db.session.rollback()
    return error_response


@app.errorhandler(InternalError)
def handle_db_internal_err(err):
    error_response = jsonify(
        code=STATUS.UNKOWN_COLUMN_ERR,
        name='Unknown column error',
        # message=str(err)
    )
    db.session.rollback()
    return error_response


@app.errorhandler(DataError)
def handle_db_data_err(err):
    error_response = jsonify(
        code=STATUS.TOO_LONG_CULUMN_ERR,
        name='Data too long for column',
        # message=str(err)
    )
    db.session.rollback()
    return error_response
