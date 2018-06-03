from aetam import app
import unittest
from flask import json
from flask import g
from aetam.models import util_db
import os

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

    def test_api_post_signup(self):
        response = self.api_post_signup({
            'username': 'name',
            'password': 'password'
        })
        self.assertEqual(200, response.status_code)
        res_json = response.get_json()
        # is valid response data?
        if res_json['errors'] != [] or len(res_json['user']) != 3 or len(res_json['status']) != 7:
            self.fail()
        self.assertEqual('name', res_json['user']['name'])

    def test_api_signup_table(self):
        posts = [
            ['name', 'password'],
            ['0123456789ABCDEF', 'password12345678'],
        ]
        self.api_post_signup_table(posts, 200)

    def test_api_signup_table_faild(self):
        posts = [
            ['0123456789ABCDEF0', 'password12345678'],
            ['0123456789ABCDEF', 'password123456789'],
        ]
        self.api_post_signup_table(posts, 400)

    def api_post_signup(self, data):
        return self.app.post(
            '/signup',
            data=json.dumps(data),
            content_type='application/json'
        )

    def api_post_signup_table(self, posts, status_code):
        for post in posts:
            self.assertEqual(
                status_code,
                self.api_post_signup({
                    'username': post[0],
                    'password': post[1]
                }).status_code
            )

    def truncate_test_db_table(self):
        with util_db.connect() as db:
            db.execute('delete from users')
            db.execute('delete from statuses')
