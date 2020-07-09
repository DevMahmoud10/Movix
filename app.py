from flask import Flask
from database.movix_db import init_movix_db
from resources.movie import movies

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movix_db'
}

init_movix_db(app)
app.register_blueprint(movies)
@app.route('/')
def index():
    return "Welcome to Movix App"

app.run()
