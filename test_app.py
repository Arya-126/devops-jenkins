import unittest
from app import app

class HomeRouteTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_returns_200_and_expected_json(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data["message"], "Goodbye!")
        self.assertEqual(data["status"], "ok")

if __name__ == "__main__":
    unittest.main()
