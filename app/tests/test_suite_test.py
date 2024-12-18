import unittest
from app.config import BACKEND_URL
import requests

# The below test cases are just to check if all the api urls are working fine
class TestSuiteTest(unittest.TestCase):

    def setUp(self):
        self.base_url = f"{BACKEND_URL}/test_suites"
        self.id = 1000

    def test_create_suite(self):
        data = {
            "name": "Test Suite Testing",
            "description": "Test suite for testing"
        }
        response = requests.post(self.base_url, json=data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.json())
        self.assertEqual(response.json()['name'], data['name'])

    def test_get_suite(self):
        response = requests.get(f"{self.base_url}/{self.id}")
        self.assertEqual(response.status_code, 400)
        self.assertIn('detail', response.json())

    def test_get_all_suites(self):
        response = requests.get(f"{self.base_url}/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_update_suite(self):
        updated_data = {
            "name": "Updated Test Suite",
            "description": "Updated description",
            "status": "inactive"
        }
        response = requests.put(f"{BACKEND_URL}/test_suites/{self.id}", json=updated_data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual( response.json().get('detail'), "Test Suit not found with id: {}".format(self.id))

    def test_delete_suite(self):
        response = requests.delete(f"{self.base_url}/{self.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual( response.json().get('message'), "Test Suit not found")
        self.assertEqual(response.json().get('id'), self.id)


if __name__ == '__main__':
    unittest.main()
