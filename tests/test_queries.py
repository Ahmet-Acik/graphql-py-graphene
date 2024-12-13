import unittest
import sys
import os

# Add the project directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import schema
from data_store import data_store

class TestQueries(unittest.TestCase):

    def setUp(self):
        # Reset the data store before each test
        data_store.clear()
        data_store.update({
            "1": {"id": "1", "name": "Ahmet Doe", "email": "ahmet@gmail.com", "password": "123456"},
            "2": {"id": "2", "name": "Mehmet Doe", "email": "mehmet@gmail.com", "password": "123456"}
        })

    def test_get_users(self):
        query = """
        {
          getUsers {
            id
            name
            email
            password
          }
        }
        """
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data["getUsers"]), 2)

    def test_get_user(self):
        query = """
        {
          getUser(id: "1") {
            id
            name
            email
            password
          }
        }
        """
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(result.data["getUser"]["id"], "1")
        self.assertEqual(result.data["getUser"]["name"], "Ahmet Doe")

if __name__ == "__main__":
    unittest.main()