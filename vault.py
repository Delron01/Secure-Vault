from password_utils import validate_pass, generate_pass, hash_password
from crypto_utils import hash_pass
from logger import log_activity
import json
import getpass

def main():
    print("="*75)
    print("Welcome to SECURE VAULT.")
    action = input("Add, View or Delete credentials? (add/view/delete)")
    if action== "add":
        site = input("site/app name: ")
        username = input("username: ")
        password = getpass.getpass("password: (leave blank to generate password) ")
        if not password:
            password = generate_pass()
            print(f"generated password: {password}")
        if not validate_pass(password):
            print("weak password.")
            return
        credentials = load_credentials()
        credentials[site] = {
            "username": username,
            "password_hash": hash_password(password)
        }
        save_credentials(credentials)
        log_activity(f"Added credentials for {site}")

    elif action == "view":
        print(json.dumps(load_credentials(), indent=2))

    elif action == "delete":
        print(json.dumps(load_credentials(), indent=2))
        site = input("site: ")
        ___ = input(f"Are you sure you want to delete {site} (y/n)")

    print("="*75)

def load_credentials():
    ...

def save_credentials():
    ...



if __name__=="__main__":
    main()