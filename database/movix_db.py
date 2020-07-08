from flask_mongoengine import MongoEngine

movix_db=MongoEngine()

def init_movix_db(app):
    movix_db.init_app(app)