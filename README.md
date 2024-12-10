# GraphQL with Graphene in Python

This project demonstrates a simple GraphQL API using the Graphene library in Python. The API allows for creating, updating, deleting, and fetching users from a hypothetical data store.

## Technologies Used

- **Python**: The programming language used for the project.
- **Graphene**: A library for building GraphQL APIs in Python.
- **GraphQL**: A query language for your API.

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

## Full Code

Here is the complete code for the project:

### app.py
```python
import graphene

# Hypothetical data store
data_store = {
    "1": {"id": "1", "name": "Ahmet Doe", "email": "ahmet@gmail.com", "password": "123456"},
    "2": {"id": "2", "name": "Mehmet Doe", "email": "mehmet@gmail.com", "password": "123456"}
}

# Define the User type
class User(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    email = graphene.String()
    password = graphene.String()

# Define the CreateUser mutation
class CreateUser(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(self, info, id, name, email, password):
        user_data = {"id": id, "name": name, "email": email, "password": password}
        data_store[id] = user_data
        return CreateUser(user=User(**user_data))

# Define the UpdateUser mutation
class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(self, info, id, name, email, password):
        user_data = data_store.get(id)
        if user_data:
            user_data.update({"name": name, "email": email, "password": password})
            data_store[id] = user_data
            return UpdateUser(user=User(**user_data))
        return UpdateUser(user=None)

# Define the DeleteUser mutation
class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(self, info, id):
        user_data = data_store.pop(id, None)
        if user_data:
            return DeleteUser(user=User(**user_data))
        return DeleteUser(user=None)

# Define the Query class
class MyQuery(graphene.ObjectType):
    user = graphene.Field(User, id=graphene.String(required=True))
    get_user = graphene.Field(User, id=graphene.String(required=True))
    get_users = graphene.List(User)

    def resolve_user(self, info, id):
        # Fetch user from your data store here
        user_data = data_store.get(id)
        if user_data:
            return User(**user_data)
        return None

    def resolve_get_user(self, info, id):
        # Fetch user from your data store here
        user_data = data_store.get(id)
        if user_data:
            return User(**user_data)
        return None

    def resolve_get_users(self, info):
        # Fetch all users from your data store here
        return [User(**user_data) for user_data in data_store.values()]

# Define the Mutation class
class MyMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

# Create the schema
schema = graphene.Schema(query=MyQuery, mutation=MyMutations)

# Function to execute and print GraphQL queries and mutations
def execute_and_print(label, query):
    print(f"\n{label}")
    result = schema.execute(query)
    if result.errors:
        print("Errors:", result.errors)
    else:
        print(result.data)

# Create a new user with a different id
execute_and_print(
    "Creating a new user with id 3:",
    """
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
)

# Update the newly created user
execute_and_print(
    "Updating the user with id 3:",
    """
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
"""
)

# Fetch all users before deleting the updated user
execute_and_print(
    "Fetching all users before deleting the user with id 3:",
    """
{
  getUsers {
    id
    name
    email
    password
  }
}
"""
)

# Delete the newly created user
execute_and_print(
    "Deleting the user with id 3:",
    """
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
"""
)

# Fetch all users after deleting the updated user
execute_and_print(
    "Fetching all users after deleting the user with id 3:",
    """
{
  getUsers {
    id
    name
    email
    password
  }
}
"""
)

# Fetch a specific user by id
execute_and_print(
    "Fetching the user with id 1:",
    """
{
  getUser(id: "1") {
    id
    name
    email
    password
  }
}
"""
)

# Fetch a specific user by id
execute_and_print(
    "Fetching the user with id 1 using user query:",
    """
{
  user(id: "1") {
    id
    name
    email
    password
  }
}
"""
)
```

## Conclusion

This project demonstrates a simple GraphQL API using Graphene in Python. It covers basic CRUD operations for user data and provides a foundation for building more complex GraphQL APIs.
