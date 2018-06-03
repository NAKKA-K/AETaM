from aetam import app
import unittest
from flask import json

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_api_post_login(self):
        response = self.app.post('/login', data={
            'username': 'name',
            'password': 'password'
        }, follow_redirects=True)
        self.assertEqual(200, response.status_code)

    def test_api_post_login_failed(self):
        response = self.app.post('/login', data={
            'username': '',
            'password': ''
        })
        self.assertEqual(400, response.status_code)

    def test_api_post_logout(self):
        response = self.app.post('/logout')
        self.assertEqual(200, response.status_code)
