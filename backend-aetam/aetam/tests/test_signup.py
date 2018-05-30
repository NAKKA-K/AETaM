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

    def setUp(self):
        self.app = app.test_client()
        util_db.init()

    def tearDown(self):
        self.truncate_test_db_table()

    def test_api_post_signup(self):
        response = self.api_post_signup({
            'username': 'name',
            'password': 'pass'
        })
        self.assertEqual(200, response.status_code)
        res_json = response.get_json()
        # is valid response data?
        if res_json['errors'] != [] or len(res_json['user']) != 2 or len(res_json['status']) != 7:
            self.fail()
        self.assertEqual('name', res_json['user']['name'])

    def api_post_signup(self, data):
        return self.app.post(
            '/signup',
            data=json.dumps(data),
            content_type='application/json'
        )

    def truncate_test_db_table(self):
        with util_db.connect() as db:
            db.execute('delete from users')
            db.execute('delete from statuses')
