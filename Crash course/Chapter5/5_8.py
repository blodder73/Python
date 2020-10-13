user_names = ['bob', 'admin', 'buddy', 'elmira', 'sofie']

for username in user_names:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")