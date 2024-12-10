from graphene import ObjectType, String, Field, List, Schema
from type import User
from mutation import CreateUser, UpdateUser, DeleteUser
from query import Query


class MyMutations(ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()


class MyQuery(ObjectType):
    user = Field(User, id=String(required=True))
    get_user = Field(User, id=String(required=True))
    get_users = List(User)

    def resolve_user(self, info, id):
        # Fetch user from your data store here
        return User(id=id, name="Example", email="example@example.com", password="password")

    def resolve_get_user(self, info, id):
        # Fetch user from your data store here
        return User(id=id, name="Example", email="example@example.com", password="password")

    def resolve_get_users(self, info):
        # Fetch all users from your data store here
        return [
            User(id="1", name="Ahmet Doe", email="ahmet@gmail.com", password="123456"),
            User(id="2", name="Mehmet Doe", email="mehmet@gmail.com", password="123456")
        ]


schema = Schema(query=MyQuery, mutation=MyMutations)

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