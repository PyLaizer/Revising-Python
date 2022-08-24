#Exercise 9.12
from user import User

class Priviledges:
    def __init__(self,*priviledges):
        self.priviledges = priviledges

    def show_priviledges(self):
        print(f"\nThe priviledges of the Admin")
        for privilege in self.priviledges:
            print(f"\n - {privilege}")    

class Admin(User):
    def __init__(self, first_name, last_name, age, username, email):
        super().__init__(first_name, last_name, age, username, email)
        self.priviledges = Priviledges("can delete user","can disable user","can add user")
