import graphene
from type import User
from data_store import data_store

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

class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(self, info, id):
        user_data = data_store.pop(id, None)
        if user_data:
            return DeleteUser(user=User(**user_data))
        return DeleteUser(user=None)