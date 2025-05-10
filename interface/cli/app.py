from controllers.authController import AuthController
from database.dbconnection import DbConnection
from database.dbapi import DbAPI
import getpass


connection = DbConnection("./database/manageit.db")
api = DbAPI(connection)


def login():
    username = input("Enter UserName: -> ")
    password = getpass.getpass("Enter Password: -> ")
    auth = AuthController()
    if auth.checkUser(username, password):
        print("Login Done")
    else:
        print("Error Login")


def register():
    name = input("Enter Full Name: -> ")
    username = input("Enter UserName: -> ")
    password = getpass.getpass("Enter Password: -> ")

    hash_password = AuthController.hashedPassword(password)

    roles = api.get("Role", "role_id, role_name")

    for role in roles:
        print(f"ID: {role[0]} - role Name: {role[1]}")

    role_id = input("Enter Role ID: -> ")
    api.insert(
        "Users",
        ("username", "password", "full_name", "role_id"),
        (username, hash_password, name, role_id),
    )


def addRole():
    role_name = input("enter Role Name: -> ")
    api.insert("Role", ("role_name",), (role_name,))


def start():
    while True:
        print("1. login")
        print("2. register")
        print("3. Add Role")

        choose = input(" Choose Action: -> ")

        match choose:
            case "1":
                login()
                break
            case "2":
                register()
                break
            case "3":
                addRole()
                break


if __name__ == "__main__":
    start()
