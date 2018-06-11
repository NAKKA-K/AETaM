import unittest
import os
from aetam import app
from aetam.models import util_db
from flask import json


class TestStatusApi(unittest.TestCase):
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

    def test_status_get_api(self):
        access = self.app.post(
            '/api/signup',
            data=json.dumps({'username':'name', 'password':'password'}),
            content_type='application/json'
        ).get_json()['user']['ACCESS_KEY']
        response = self.app.get(
            '/api/statuses',
            data=json.dumps({'ACCESS_KEY':access}),
            content_type='application/json'
        )
        self.assertEqual(200, response.status_code)
        if response.get_json()['errors'] != []:
            self.fail()

    def truncate_test_db_table(self):
        with util_db.connect() as db:
            db.execute('delete from Users')
            db.execute('delete from Statuses')
