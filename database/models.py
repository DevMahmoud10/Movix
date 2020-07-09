from .movix_db import movix_db
from flask_bcrypt import generate_password_hash, check_password_hash


class Movie(movix_db.Document):
    name = movix_db.StringField(required=True, unique=True)
    casts = movix_db.ListField(movix_db.StringField(), required=True)
    genres = movix_db.ListField(movix_db.StringField(), required=True)
    added_by = movix_db.ReferenceField('User')


class User(movix_db.Document):
    email = movix_db.EmailField(required=True, unique=True)
    password = movix_db.StringField(required=True, min_length=6)
    movies = movix_db.ListField(movix_db.ReferenceField(
        'Movie', reverse_delete_rule=movix_db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, other_password):
        return check_password_hash(self.password, other_password)


User.register_delete_rule(Movie, 'added_by', movix_db.CASCADE)
