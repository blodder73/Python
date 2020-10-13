#user_names = ['bob', 'admin', 'buddy', 'elmira', 'sofie']
user_names = []

if user_names:
    for username in user_names:
        if username == 'admin':
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")