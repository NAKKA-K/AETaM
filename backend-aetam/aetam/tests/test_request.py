from aetam import app
import unittest

class TestResponseGet(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_index_page(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)

    def test_get_login_page(self):
        response = self.app.get('/login')
        self.assertEqual(200, response.status_code)

