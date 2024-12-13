# GraphQL with Graphene in Python

This project demonstrates a simple GraphQL API using the Graphene library in Python. The API allows for creating, updating, deleting, and fetching users from a hypothetical data store.

## Technologies Used

- **Python**: The programming language used for the project.
- **Graphene**: A library for building GraphQL APIs in Python.
- **GraphQL**: A query language for your API.
- **unittest**: A built-in Python module for testing.

## Project Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/graphql-py-graphene.git
    cd graphql-py-graphene
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```sh
    pip install graphene
    ```

## Project Structure

- `app.py`: The main application file that defines the GraphQL schema and executes queries and mutations.
- `data_store.py`: Contains the hypothetical data store used for storing user data.
- `type.py`: Defines the `User` type used in the GraphQL schema.
- `mutation.py`: Contains the mutation classes for creating, updating, and deleting users.
- `tests/`: Contains the unit tests for the GraphQL API.


## Data Store

The data store is a simple dictionary that holds user data. It is defined within the `app.py` file:

```python
data_store = {
    "1": {"id": "1", "name": "Ahmet Doe", "email": "ahmet@gmail.com", "password": "123456"},
    "2": {"id": "2", "name": "Mehmet Doe", "email": "mehmet@gmail.com", "password": "123456"}
}
```

## Operations

### Create a User



Mutation

 to create a new user:
```graphql
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
```

### Update a User

Mutation to update an existing user:
```graphql
mutation {
  updateUser(id: "3", name: "John Updated", email: "john_updated@gmail.com", password: "newpassword") {
    user {
      id
      name
      email
      password
    }
  }
}
```

### Delete a User

Mutation to delete an existing user:
```graphql
mutation {
  deleteUser(id: "3") {
    user {
      id
      name
      email
      password
    }
  }
}
```

### Fetch All Users

Query to fetch all users:
```graphql
{
  getUsers {
    id
    name
    email
    password
  }
}
```

### Fetch a User by ID

Query to fetch a specific user by ID:
```graphql
{
  getUser(id: "1") {
    id
    name
    email
    password
  }
}
```

## Running the Application

To run the application, execute the `app.py` file:
```sh
python -u "/path/to/your/project/app.py"
```

## Running the Tests

To run the  tests, execute the following command:
```sh
python -m unittest discover tests
```

You should see output similar to the following:
```
Creating a new user with id 3:
{'createUser': {'user': {'id': '3', 'name': 'John Doe', 'email': 'john@gmail.com', 'password': 'abcdef'}}}

Updating the user with id 3:
{'updateUser': {'user': {'id': '3', 'name': 'John Updated', 'email': 'john_updated@gmail.com', 'password': 'newpassword'}}}

Fetching all users before deleting the user with id 3:
{'getUsers': [{'id': '1', 'name': 'Ahmet Doe', 'email': 'ahmet@gmail.com', 'password': '123456'}, {'id': '2', 'name': 'Mehmet Doe', 'email': 'mehmet@gmail.com', 'password': '123456'}, {'id': '3', 'name': 'John Updated', 'email': 'john_updated@gmail.com', 'password': 'newpassword'}]}

Deleting the user with id 3:
{'deleteUser': {'user': {'id': '3', 'name': 'John Updated', 'email': 'john_updated@gmail.com', 'password': 'newpassword'}}}

Fetching all users after deleting the user with id 3:
{'getUsers': [{'id': '1', 'name': 'Ahmet Doe', 'email': 'ahmet@gmail.com', 'password': '123456'}, {'id': '2', 'name': 'Mehmet Doe', 'email': 'mehmet@gmail.com', 'password': '123456'}]}

Fetching the user with id 1:
{'getUser': {'id': '1', 'name': 'Ahmet Doe', 'email': 'ahmet@gmail.com', 'password': '123456'}}

Fetching the user with id 1 using user query:
{'user': {'id': '1', 'name': 'Ahmet Doe', 'email': 'ahmet@gmail.com', 'password': '123456'}}
```


## Conclusion

This project demonstrates a simple GraphQL API using Graphene in Python. It covers basic CRUD operations for user data and provides a foundation for building more complex GraphQL APIs.
