from aetam import app
import unittest
from flask import json

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_api_post_login(self):
        response = self.api_post_login({
            'username': 'name',
            'password': 'pass'
        })
        self.assertEqual(200, response.status_code)
        self.assertEqual([], response.get_json()['errors'])

    def test_api_post_login_failed(self):
        response = self.api_post_login({
            'username': '',
            'password': ''
        })
        self.assertEqual(400, response.status_code)
        self.assertIn('Invalid username', response.get_json()['errors'])

    def api_post_login(self, data):
        return self.app.post('/login',
                data=json.dumps(data),
                content_type='application/json')

    def test_api_post_logout(self):
        response = self.app.post('/logout')
        self.assertEqual(200, response.status_code)
        self.assertEqual([], response.get_json()['errors'])
