#Exercise 9 : Classes
#                   C           L           A           S           S           E           S

#Exercise 9.1

class Restaurant:
    def __init__(self,res_name,cuisine_type):
        self.restaurant_name = res_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\nThe name of the restaurant is : {self.restaurant_name}")
        print(f"Your cuisine is: {self.cuisine}")    

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open !  !  !")

    def set_number_served(self,no):
        self.number_served = no

    def increment_number_served(self,served_no):
        self.number_served += served_no 


restaurant = Restaurant('Jeremys','American Cuisine')
print(restaurant.restaurant_name)
print(restaurant.cuisine)
restaurant.describe_restaurant()
restaurant.open_restaurant()      


#Exercise 9.2

restaurant1 = Restaurant("Krusty Krabs","United Kingdom Cuisine")
restaurant1.describe_restaurant()

restaurant2 = Restaurant("Mama Put","Nigerian Cuisine")
restaurant2.describe_restaurant()

restaurant3 = Restaurant("Halal food","Indian Cuisine")
restaurant3.describe_restaurant()


#Exercise 9.3

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


user1 = User("Dele","Bakare",32,"thechieflearner01","delebakare01@gmail.com")
user1.describe_user()
user1.greet_user()

user2 = User("Favour","Chukwedo",31,"favourthegreat","fchukwedo01@gmail.com")
user2.describe_user()
user2.greet_user()

user3 = User("Caleb","Tolorunleke",24,"Kalebbababa","ctolorunleke@gmail.com")
user3.describe_user()
user3.greet_user()


#Exercise 9.4
# Using Exercise 9.1

restaurant4 = Restaurant("The Indians","Any Indian Cuisine")
restaurant4.describe_restaurant()
restaurant4.open_restaurant()
print(restaurant4.number_served)  

restaurant4.number_served = 3
print(restaurant4.number_served)

restaurant4.set_number_served(23)
print(restaurant4.number_served)

restaurant4.increment_number_served(11)
print(restaurant4.number_served)


#Exercise 9.5
#Using Exercise 9.3

user4 = User("Abraham","Lawson",20,"Horla mide","lawsonabraham@yahoo.com")
user4.describe_user()
user4.greet_user()
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.reset_login_attempts()
print(user4.login_attempts)
