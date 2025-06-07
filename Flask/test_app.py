import unittest
from app import app  # Make sure your Flask file is named app.py

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello from Docker!", response.data)

    def test_health_route(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertIn("status", json_data)
        self.assertEqual(json_data["status"], "healthy")
        self.assertIn("timestamp", json_data)

if __name__ == '__main__':
    unittest.main()
