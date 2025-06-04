import unittest
from fastapi.testclient import TestClient
from fast_api import app

class FastApiTestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_hello_world(self):
        response = self.client.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'hello world!'})

if __name__ == '__main__':
    unittest.main()
