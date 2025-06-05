import unittest
from hello_api import app

class HelloApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        response = self.app.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "Hello, Codex!")

if __name__ == '__main__':
    unittest.main()
