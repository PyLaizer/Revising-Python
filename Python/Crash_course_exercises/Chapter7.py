#Exercise 7: User INput AND WHILE LOOPS

#       U      S    E     R       I   N   P   U   T 

#7.1
rentalCar = input("What kind of rental car would you like: ")
print(f"\nLet me see if I can find you a {rentalCar}")

#7.2
restaurantSeating = input("How many people are in this dinner group: ")
restaurantSeating = int(restaurantSeating)
if restaurantSeating > 8:
    print("You will have to wait for a table")
else:
    print("Your table is ready")   

#7.3
mul_of_ten = input("Enter a number: ")   
mul_of_ten = int(mul_of_ten)  
if mul_of_ten % 10 == 0:
    print("This digit is a multiple of 10")
else:
    print("This digit is not a multiple of 10") 


#           W   H   I   L   E       L   O   O   P   S
#7.4
pizza_toppings = "\nEnter a pizza topping: "
pizza_toppings += "\n Type 'quit' to end program: "

pizza_request = "",
while pizza_request != 'quit':
    pizza_request = input(pizza_toppings)
    if pizza_request != 'quit':
        print(f"This {pizza_request} topping has been added to your pizza.")

#7.5
age = "\nEnter your age: "
age += "\nType 'quit' to exit the program: "

person_age = ""
while person_age != 'quit':
    person_age = input(age)
    if person_age != 'quit':
        person_age = int(person_age)
        if person_age < 3:
            print("The ticket is free for you")
        elif person_age <= 12:
            print("The ticket is $10")  
        else:
            print("The ticket is $15")


