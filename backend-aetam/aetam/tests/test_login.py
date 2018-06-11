from aetam import app
import unittest
from flask import json
import os
from aetam.models import util_db

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.set_test_db()

    @classmethod
    def set_test_db(cls):
        app.config['DATABASE'] = os.path.join(app.config['BASE_DIR'], 'test.sqlite3')
        util_db.init()

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        self.truncate_test_db_table()

    # Post signup before login
    def test_api_post_login(self):
        self.app.post(
            '/api/signup',
            data=json.dumps({'username': 'name', 'password': 'password'}),
            content_type='application/json'
        )
        response = self.app.post('/login', data={
            'username': 'name',
            'password': 'password'
        }, follow_redirects=True)
        self.assertEqual(200, response.status_code)

    def test_api_post_login_not_exist(self):
        response = self.app.post('/login', data={
            'username': 'name',
            'password': 'password'
        }, follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertIn(b'Not found user or pass', response.data)

    def test_api_post_login_failed(self):
        response = self.app.post('/login', data={
            'username': '',
            'password': ''
        })
        self.assertEqual(400, response.status_code)

    def test_api_post_logout(self):
        response = self.app.post('/logout')
        self.assertEqual(200, response.status_code)

    def truncate_test_db_table(self):
        with util_db.connect() as db:
            db.execute('delete from Users')
            db.execute('delete from Statuses')
