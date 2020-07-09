from flask import Response, request
from database.models import Movie, User
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

class MoviesApi(Resource):
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        body = request.get_json()
        user_id = get_jwt_identity()
        user = User.objects.get(id=user_id)
        movie = Movie(**body,added_by=user)
        movie.save()
        user.update(push__movies=movie)
        user.save()
        return {'ID': str(movie.id)}, 200


class MovieApi(Resource):
    @jwt_required
    def put(self, movie_id):
        body = request.get_json()
        user_id = get_jwt_identity()
        movie = Movie.objects.get(id=movie_id, added_by=user_id)
        Movie.objects.get(id=movie_id).update(**body)
        return '', 200

    @jwt_required
    def delete(self, movie_id):
        user_id = get_jwt_identity()
        movie = Movie.objects.get(id=movie_id, added_by=user_id)
        movie.delete()
        return '', 200

    def get(self, movie_id):
        movies = Movie.objects.get(id=movie_id).to_json()
        return Response(movies, mimetype="application/json", status=200)
