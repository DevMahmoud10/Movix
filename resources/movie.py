from flask import Blueprint, request, Response
from database.models import Movie

movies = Blueprint('movies', __name__)

@movies.route('/movies')
def list_movies():
    movies_list=Movie.objects().to_json()
    return Response(movies_list, mimetype="application/json", status=200)

@movies.route('/movies/<movie_id>')
def get_movie(movie_id):
    movie = Movie.objects.get(id=movie_id).to_json()
    return Response(movie, mimetype="application/json", status=200)

@movies.route('/add_movie', methods=['POST'])
def add_movie():
    response_data=request.get_json()
    movie=Movie(**response_data).save()
    return {'ID': str(movie.id)},200

@movies.route('/update_movie/<movie_id>', methods=['PUT'])
def update_movie(movie_id):
    response_data=request.get_json()
    Movie.objects.get(id=movie_id).update(**response_data)
    return {'ID': movie_id},200

@movies.route('/delete_movie/<movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    Movie.objects.get(id=movie_id).delete()
    return {'ID': movie_id},200