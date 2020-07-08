from flask import Flask, request, Response
from database.movix_db import init_movix_db
from database.models import Movie

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movix_db'
}

init_movix_db(app)


@app.route('/')
def index():
    return "Welcome to Movix App"


@app.route('/movies')
def list_movies():
    movies_list=Movie.objects().to_json()
    return Response(movies_list, mimetype="application/json", status=200)

@app.route('/movies/<movie_id>')
def get_movie(movie_id):
    movie = Movie.objects.get(id=movie_id).to_json()
    return Response(movie, mimetype="application/json", status=200)

@app.route('/add_movie', methods=['POST'])
def add_movie():
    response_data=request.get_json()
    movie=Movie(**response_data).save()
    return {'ID': str(movie.id)},200

@app.route('/update_movie/<movie_id>', methods=['PUT'])
def update_movie(movie_id):
    response_data=request.get_json()
    Movie.objects.get(id=movie_id).update(**response_data)
    return {'ID': movie_id},200

@app.route('/delete_movie/<movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    Movie.objects.get(id=movie_id).delete()
    return {'ID': movie_id},200

app.run()
