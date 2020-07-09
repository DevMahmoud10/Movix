from .movie import MoviesApi, MovieApi
from .auth import SignupApi, LoginApi


def init_routes(api):
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(MovieApi, '/api/movies/<movie_id>')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')