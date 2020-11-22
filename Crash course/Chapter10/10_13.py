import json


def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        answer = input(f"Are you {username}? (yes/no) ")
        if answer == "yes":
            print(f"Welcome back {username}!")
        elif answer == "no":
            username = get_new_username()
        else:
            answer = input(f"I did not understand your answer, are you {username}? (yes/no) ")
    else:
        username = get_new_username()
        print(f"We'll remember you when you com back, {username}!")


greet_user()