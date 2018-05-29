from aetam import app
import unittest
from flask import json

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    # TODO: 開発時のテスト用にAPI以外の形式で操作できるようにしている
    def test_post_login(self):
        response = self.app.post('/login',data={
            'username': 'name',
            'password': 'pass'
        }, follow_redirects=True)
        self.assertEqual(200, response.status_code)

    def test_api_post_login(self):
        response = self.api_post_login({
            'username': 'name',
            'password': 'pass'
        })
        self.assertEqual(200, response.status_code)
        self.assertEqual('Logged in!', response.get_json()['message'])

    def test_api_post_login_failed(self):
        response = self.api_post_login({
            'username': '',
            'password': ''
        })
        self.assertEqual(400, response.status_code)
        self.assertEqual('Invalid username', response.get_json()['error'])

    def api_post_login(self, data):
        return self.app.post('/login',
                data=json.dumps(data),
                content_type='application/json')
