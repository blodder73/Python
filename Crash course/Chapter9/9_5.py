class User:

    def __init__(self, first_name, last_name, age, login_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_name = login_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"fullname:\t{self.first_name} {self.last_name}")
        print(f"age:\t\t{self.age}")
        print(f"login:\t\t{self.login_name}")

    def greet_user(self):
        print(f"Hello {self.first_name}")

    def increment_login(self):
        self.login_attempts += 1

    def reset_login(self):
        self.login_attempts = 0


user1 = User('Buddy', 'Lodder', 46, 'blodder')
user2 = User('Elmira', 'Lodder', 34, 'elodder')

user1.describe_user()
user2.describe_user()

print()
user1.greet_user()
user2.greet_user()

print(f"User {user1.first_name} has {user1.login_attempts} login attempts")
user1.increment_login()
print(f"User {user1.first_name} has {user1.login_attempts} login attempts")
user1.increment_login()
print(f"User {user1.first_name} has {user1.login_attempts} login attempts")
user1.increment_login()
print(f"User {user1.first_name} has {user1.login_attempts} login attempts")
user1.reset_login()
print(f"User {user1.first_name} has {user1.login_attempts} login attempts")