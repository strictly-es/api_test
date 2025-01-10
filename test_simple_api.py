import unittest
from simple_api import app

class SimpleApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_fixed_value(self):
        response = self.app.get('/api/fixed')
        self.assertEqual(response.status_code, 200)
        self.assertIn("random_number", response.json)
        self.assertIsInstance(response.json["random_number"], int)
        self.assertGreaterEqual(response.json["random_number"], 1)
        self.assertLessEqual(response.json["random_number"], 50)

if __name__ == '__main__':
    unittest.main()