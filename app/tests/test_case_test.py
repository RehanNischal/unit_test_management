import unittest

from app.config import BACKEND_URL
import requests

# The below test cases are just to check if all the api urls are working fine
class TestCaseTest(unittest.TestCase):

    def setUp(self):
        self.base_url = f"{BACKEND_URL}/test_cases"
        self.test_suit_id = 1000
        self.id = 1000

    def test_create_case(self):
        data = {
          "name": "Test case testing",
          "description": "Test case testing",
          "priority": "high",
          "expected_outcome": "User should successfully log in",
          "test_suite_id": self.test_suit_id
        }
        response = requests.post(self.base_url, json=data)

        self.assertEqual(response.status_code, 400)
        self.assertIn('detail', response.json())
        self.assertEqual(response.json()['detail'], "400: Test Suite with id {} does not exist".format(self.test_suit_id))

    def test_get_case(self):
        response = requests.get(f"{self.base_url}/{self.id}")
        self.assertEqual(response.status_code, 400)
        self.assertIn('detail', response.json())

    def test_update_case(self):
        updated_data = {
            "name": "Test case testing",
            "description": "Test case testing",
            "priority": "high",
            "expected_outcome": "User should successfully log in",
            "status": "active"
        }
        response = requests.put(f"{BACKEND_URL}/test_cases/{self.id}", json=updated_data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual( response.json().get('detail'), "Test Case not found with id: {}".format(self.id))

    def test_delete_case(self):
        response = requests.delete(f"{self.base_url}/{self.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual( response.json().get('message'), "Test Case not found")
        self.assertEqual(response.json().get('id'), self.id)

    def test_search_case(self):
        response = requests.get(f"{self.base_url}/search/", params={"keyword":"testing"})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)


if __name__ == '__main__':
    unittest.main()
