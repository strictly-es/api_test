import unittest
from simple_api import app

class SimpleApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_fixed_value(self):
        response = self.app.get('/api/fixed')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "This is a fixed response!!"})

if __name__ == '__main__':
    unittest.main()