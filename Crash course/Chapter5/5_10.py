current_users = ['bob', 'admin', 'buddy', 'elmira', 'sofie']
new_users = ['mira', 'Admin', 'buddy', 'ryuken', 'jack']

for user in new_users:
    if user.lower() in current_users:
        print(f"Please enter a new username {user}")
    else:
        print(f"username {user} is still available.")