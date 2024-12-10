import graphene
from type import User

class Query(graphene.ObjectType):
    user = graphene.Field(User, id=graphene.String())
    get_user = graphene.Field(User, id=graphene.String())
    get_users = graphene.List(User)

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