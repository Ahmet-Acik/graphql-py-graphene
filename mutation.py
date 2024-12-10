import graphene
from type import User

class CreateUser(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(self, info, id, name, email, password):
        user = User(id=id, name=name, email=email, password=password)
        # Add user to your data store here
        return CreateUser(user=user)

class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(self, info, id, name, email, password):
        user = User(id=id, name=name, email=email, password=password)
        # Update user in your data store here
        return UpdateUser(user=user)

class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(self, info, id):
        user = User(id=id, name="", email="", password="")
        # Delete user from your data store here
        return DeleteUser(user=user)