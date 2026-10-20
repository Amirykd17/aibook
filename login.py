# create a login in python
import getpass
import secrets

USERS = {
    "admin": "password123",
}

MAX_ATTEMPTS = 3


def login() -> bool:
    for attempt in range(1, MAX_ATTEMPTS + 1):
        username = input("Username: ").strip()
        password = getpass.getpass("Password: ")

        expected = USERS.get(username)
        if expected and secrets.compare_digest(password, expected):
            print(f"Welcome, {username}.")
            return True

        remaining = MAX_ATTEMPTS - attempt
        if remaining:
            print(f"Invalid username or password. {remaining} attempt(s) left.")
        else:
            print("Too many failed attempts. Access denied.")

    return False


if __name__ == "__main__":
    login()
