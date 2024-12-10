import graphene

class User(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    email = graphene.String()
    password = graphene.String()