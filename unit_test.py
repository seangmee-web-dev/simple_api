import unittest
from main import app
from fastapi.testclient import TestClient

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
    def true_when_x_is_17(self):
        response = self.client.get("/is_prime/17")
        self.assertEqual(response.status_code)
        self.assertTrue(response.json())
    def true_when_x_is_36(self):
        response = self.client.get("/is_prime/36")
        self.assertEqual(response.status_code)
        self.assertTrue(response.json())
    def true_when_x_is_13219(self):
        response = self.client.get("/is_prime/13219")
        self.assertEqual(response.status_code)
        self.assertTrue(response.json())
    def test_plus_5_6(self):
        response = self.client.get("/plus/5/6")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 11})
    def test_plus_8_8(self):
        response = self.client.get("/plus/8/8")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 16})
        
if __name__ == "__main__":
    unittest.main()