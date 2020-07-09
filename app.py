from flask import Flask
from database.movix_db import init_movix_db
from resources.routes import init_routes
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movix_db'}

init_movix_db(app)
init_routes(api)

app.run()
