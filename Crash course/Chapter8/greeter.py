def greet_general():
    """"Display a simple greeting."""
    print("Hello!")

def greet_user(username):
    """"Display a simple personalized greeting."""
    print(f"Hello, {username.title()}!")

greet_general()

greet_user("Buddy")