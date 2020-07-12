import unittest
import json

from app import app
from database.movix_db import movix_db


class SignupTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = movix_db.get_db()

    def test_successful_signup(self):
        # given
        payload = json.dumps({
            "email": "testsignup@mail.com",
            "password": "testsignuppassword"
        })
        # when
        response = self.app.post(
            '/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)
        # then
        self.assertEqual(200, response.status_code)
        self.assertEqual(str, type(response.json['id']))

    def test_signup_with_existing_email(self):
        # given
        payload = json.dumps({
            "email": "testsignup@mail.com",
            "password": "testsignuppassword"
        })
        # when
        self.app.post(
            '/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)
        response = self.app.post(
            '/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)
        # then
        self.assertEqual(400, response.status_code)

    def test_signup_with_invalid_email(self):
        # given
        payload = json.dumps({
            "email": "invalidemail",
            "password": "testsignuppassword"
        })
        # when
        response = self.app.post(
            '/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)
        # then
        self.assertEqual(500, response.status_code)

    def test_signup_without_email(self):
        # given
        payload = json.dumps({
            "password": "testsignuppassword"
        })
        # when
        response = self.app.post(
            '/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)
        # then
        self.assertEqual(500, response.status_code)

    def test_signup_with_invalid_password(self):
        # given
        payload = json.dumps({
            "email": "invalidemail",
        })
        # when
        response = self.app.post(
            '/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)
        # then
        self.assertEqual(500, response.status_code)

    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
