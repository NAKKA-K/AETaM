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

    def setUp(self):
        self.app = app.test_client()
        self.create_test_db()

    def tearDown(self):
        self.truncate_test_db_table()

    def test_api_post_signup(self):
        response = self.api_post_signup({
            'username': 'name',
            'password': 'pass'
        })
        self.assertEqual(200, response.status_code)
        self.assertEqual([], response.get_json()['errors'])
        #self.assertEqual(2, len(response.get_json()['user']))
        #self.assertEqual('name', response.get_json()['user']['name'])
        #self.assertEqual(7, len(response.get_json()['status']))

    def api_post_signup(self, data):
        return self.app.post('/signup',
                data=json.dumps(data),
                content_type='application/json')

    def truncate_test_db_table(self):
        with util_db.connect() as db:
            cur = db.execute('select * from users')
            for line in cur.fetchall():
                print(line[0])

    @classmethod
    def set_test_db(cls):
        app.config['DATABASE'] = os.path.join(app.config['BASE_DIR'], 'test.sqlite3')

    def create_test_db(self):
        util_db.init()

