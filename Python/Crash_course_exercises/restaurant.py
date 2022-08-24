#Exercise 9.10
"""A class that can be used to represent a restaurant"""

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
        return self.number_served

    def increment_number_served(self,served_no):
        self.number_served += served_no 
