from flask import Flask
from database.movix_db import init_movix_db

from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from resources.errors import errors
from flask_mail import Mail

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
mail= Mail(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movix_db'}
    
from resources.routes import init_routes
init_movix_db(app)
init_routes(api)