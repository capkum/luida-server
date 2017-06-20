from flask import Flask
from user import users
from user.models import db


app = Flask(__name__)
app.config.from_object('settings')
app.register_blueprint(users)
db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=8000)
