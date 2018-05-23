from aetam import app
import unittest

class TestResponseGet(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_index_page(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)


if __name__ == "__main__":
    unittest.main()
