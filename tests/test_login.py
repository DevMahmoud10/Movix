import unittest
import json

from app import app
from database.movix_db import movix_db


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = movix_db.get_db()

    def test_successful_signup(self):
        # given
        email = "testlogin@mail.com"
        password = "testloginpassword"
        user_payload = json.dumps({
            "email": email,
            "password": password
        })

        self.app.post('/api/auth/signup',
                      headers={"Content-Type": "application/json"}, data=user_payload)
        response = self.app.post(
            '/api/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['token']

        movie_payload = {
            "name": "Star Wars 2017",
            "casts": ["Daisy Ridley", "Adam Driver"],
            "genres": ["Fantasy", "Sci-fi"]
        }
        # When
        response = self.app.post('/api/movies',
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(movie_payload))

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(str, type(response.json['ID']))

    def test_login_with_invalid_email(self):
        # given
        signup_payload = json.dumps({
            "email": "testlogin@mail.com",
            "password": "testloginpassword"
        })

        self.app.post('/api/auth/signup',
                      headers={"Content-Type": "application/json"}, data=signup_payload)
        login_payload = json.dumps({
            "email": "invalid_email",
            "password": "invalidpassword"
        })           
        response = self.app.post(
            '/api/auth/login', headers={"Content-Type": "application/json"}, data=login_payload)

        # Then
        self.assertEqual(401, response.status_code)

    def test_login_with_invalid_password(self):
        # given
        signup_payload = json.dumps({
            "email": "testlogin@mail.com",
            "password": "testloginpassword"
        })

        self.app.post('/api/auth/signup',
                      headers={"Content-Type": "application/json"}, data=signup_payload)
        login_payload = json.dumps({
            "email": "testlogin@mail.com",
            "password": "invalidpassword"
        })           
        response = self.app.post(
            '/api/auth/login', headers={"Content-Type": "application/json"}, data=login_payload)

        # Then
        self.assertEqual(401, response.status_code)

    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)

    
