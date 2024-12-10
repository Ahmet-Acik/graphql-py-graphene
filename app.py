import graphene
from type import User
from mutation import CreateUser, UpdateUser, DeleteUser

# Hypothetical data store
data_store = {
    "1": {"id": "1", "name": "Ahmet Doe", "email": "ahmet@gmail.com", "password": "123456"},
    "2": {"id": "2", "name": "Mehmet Doe", "email": "mehmet@gmail.com", "password": "123456"}
}

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

def execute_and_print(query):
    result = schema.execute(query)
    if result.errors:
        print("Errors:", result.errors)
    else:
        print(result.data)

execute_and_print(
    """
mutation {
  createUser(id: "2", name: "Mehmet Doe", email: "mehmet@gmail.com", password: "123456") {
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

execute_and_print(
    """
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
)

execute_and_print(
    """
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
)

execute_and_print(
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

execute_and_print(
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

execute_and_print(
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