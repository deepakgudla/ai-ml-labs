import unittest
import app

class ServerTest(unittest.TestCase):
    def test_server(self):
        test_ = app.app.test_client(self)
        response = test_.get('/', content_type = 'html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello', response.data)
               
if __name__ == '__main':
    unittest.main
