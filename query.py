import graphene
from type import User

# Hypothetical data store
data_store = {
    "1": {"id": "1", "name": "Ahmet Doe", "email": "ahmet@gmail.com", "password": "123456"},
    "2": {"id": "2", "name": "Mehmet Doe", "email": "mehmet@gmail.com", "password": "123456"}
}

class Query(graphene.ObjectType):
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