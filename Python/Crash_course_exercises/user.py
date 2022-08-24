#Exercise 9.12
class User:
    def __init__(self,first_name,last_name,age,username,email):
        self.f_name = first_name
        self.l_name = last_name
        self.age = age
        self.username = username
        self.email = email
        self.login_attempts = 0

    def describe_user(self):  
        print("\nInformation for this user")
        print(f"First Name: {self.f_name}")
        print(f"Last Name: {self.l_name}")
        print(f"Username: {self.username}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"\nGood Morning: {self.f_name} {self.l_name}")      

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"You just logged in {self.login_attempts} times")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"\nYour Login attempt is now {self.login_attempts}")