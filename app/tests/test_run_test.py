import unittest

from app.config import BACKEND_URL
import requests

# The below test cases are just to check if all the api urls are working fine
class TestRunTest(unittest.TestCase):

    def setUp(self):
        self.base_url = f"{BACKEND_URL}/test_runs"
        self.test_suit_id = 1000
        self.id = 1000

    def test_create_run(self):
        data = {
          "run_status": "in_progress",
          "test_suite_id": self.test_suit_id
        }
        response = requests.post(self.base_url, json=data)

        self.assertEqual(response.status_code, 400)
        self.assertIn('detail', response.json())
        self.assertEqual(response.json()['detail'], "400: Test Suite with id {} does not exist".format(self.test_suit_id))

    def test_get_run(self):
        response = requests.get(f"{self.base_url}/{self.id}")
        self.assertEqual(response.status_code, 400)
        self.assertIn('detail', response.json())

    def test_get_all_runs(self):
        response = requests.get(f"{self.base_url}/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_update_run(self):
        updated_data = {
            "result": "Failed",
            "end_time": "2024-12-16T17:38:43.970Z",
            "run_status": "complete"
        }
        response = requests.put(f"{BACKEND_URL}/test_runs/{self.id}", json=updated_data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual( response.json().get('detail'), "Test Run not found with id: {}".format(self.id))

    def test_delete_run(self):
        response = requests.delete(f"{self.base_url}/{self.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual( response.json().get('message'), "Test Run not found")
        self.assertEqual(response.json().get('id'), self.id)


if __name__ == '__main__':
    unittest.main()
