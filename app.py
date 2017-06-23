import http

from flask import Flask, jsonify
from api.database import db
from api.users import users
from api.product import productor_profile
from flask_migrate import Migrate


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


app = Flask(__name__)
app.config.from_object('settings')
app.register_blueprint(users)
app.register_blueprint(productor_profile)
db.init_app(app)
# migrate
migrate = Migrate(app, db)


def error_handler(err):
    """error to JSON format"""
    error_response = jsonify(
        code=getattr(err, 'code', http.client.INTERNAL_SERVER_ERROR),
        name=getattr(err, 'name', 'Unknown'),
        message=getattr(err, 'description', '')
    )
    return error_response


for error in TARGET_HTTP_ERROR_CODES:
  app.register_error_handler(error, error_handler)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
