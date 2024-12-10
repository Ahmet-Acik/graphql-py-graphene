import graphene
from type import User
from mutation import CreateUser, UpdateUser, DeleteUser
from data_store import data_store

class MyMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

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

schema = graphene.Schema(query=MyQuery, mutation=MyMutations)

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