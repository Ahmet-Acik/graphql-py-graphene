import unittest
import sys
import os

# Add the project directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import schema
from data_store import data_store

class TestMutations(unittest.TestCase):

    def setUp(self):
        # Reset the data store before each test
        data_store.clear()
        data_store.update({
            "1": {"id": "1", "name": "Ahmet Doe", "email": "ahmet@gmail.com", "password": "123456"},
            "2": {"id": "2", "name": "Mehmet Doe", "email": "mehmet@gmail.com", "password": "123456"}
        })

    def test_create_user(self):
        query = """
        mutation {
          createUser(id: "3", name: "John Doe", email: "john@gmail.com", password: "abcdef") {
            user {
              id
              name
              email
              password
            }
          }
        }
        """
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(result.data["createUser"]["user"]["id"], "3")
        self.assertEqual(result.data["createUser"]["user"]["name"], "John Doe")

    def test_update_user(self):
        query = """
        mutation {
          updateUser(id: "2", name: "Mehmet Updated", email: "mehmet_updated@gmail.com", password: "newpassword") {
            user {
              id
              name
              email
              password
            }
          }
        }
        """
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(result.data["updateUser"]["user"]["id"], "2")
        self.assertEqual(result.data["updateUser"]["user"]["name"], "Mehmet Updated")

    def test_delete_user(self):
        query = """
        mutation {
          deleteUser(id: "2") {
            user {
              id
              name
              email
              password
            }
          }
        }
        """
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(result.data["deleteUser"]["user"]["id"], "2")
        self.assertEqual(result.data["deleteUser"]["user"]["name"], "Mehmet Doe")

if __name__ == "__main__":
    unittest.main()