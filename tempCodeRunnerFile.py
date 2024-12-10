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