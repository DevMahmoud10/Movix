from .movix_db import movix_db

class Movie(movix_db.Document):
    name = movix_db.StringField(required=True, unique=True)
    casts = movix_db.ListField(movix_db.StringField(), required=True)
    genres = movix_db.ListField(movix_db.StringField(), required=True)