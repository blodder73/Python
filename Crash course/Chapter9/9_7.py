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


class Admin(User):

    def __init__(self, first_name, last_name,  age, login_name):
        super().__init__(first_name, last_name, age, login_name)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Login {self.login_name} has privilege: {self.privileges[0], self.privileges[1], self.privileges[2]}")


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
print()

user_admin = Admin('admin', 'admin', 0, 'admin')

print(f"User {user_admin.login_name} has privileges:")
Admin.show_privileges(user_admin)