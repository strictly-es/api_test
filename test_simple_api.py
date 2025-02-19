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
        self.assertLessEqual(response.json["random_number"], 100)

    def test_hash_string(self):
        response = self.app.post('/api/hash', json={"input_string": "test"})
        self.assertEqual(response.status_code, 200)
        expected_hash = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
        self.assertEqual(response.json["hashed_value"], expected_hash)

if __name__ == '__main__':
    unittest.main()
        