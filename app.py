from flask import Flask
from api.product import productor_profile
from api.users import users
from api.users.models import db
from api.auth import auth
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('settings')
app.register_blueprint(users)
app.register_blueprint(auth)
app.register_blueprint(productor_profile)
db.init_app(app)
# migrate
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
