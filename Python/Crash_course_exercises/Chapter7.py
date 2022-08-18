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

#7.6
# Using Exercise 7.4

pizza_toppings = "\nEnter a pizza topping: "
pizza_toppings += "\n Type 'quit' to end program: "
pizza_request = "",
active = True
while active:
    pizza_request = input(pizza_toppings)
    if pizza_request != 'quit':
        print(f"This {pizza_request} topping has been added to your pizza.")
    else:
        active = False
        break    

#7.7 DO NOT UNCOMMENT  ! ! ! It's gonna run INFINITELY
# num = 12
# while num < 30:
#     print(f"{num} is less than 30") 

#7.8 
sandwich_orders = ["Chicken Sandwich","Egg Sandwich","Meatball Sandwich","Roast Beef Sandwich","Grilled Chesse Sandwich"] 
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"\nI made you a {sandwich}") 
    finished_sandwiches.append(sandwich)

print("\nHere is the list of made sandwiches:")
for made_sandwich in finished_sandwiches:
    print(f"\n  {made_sandwich}")

#7.9
sandwich_orders = ["Pastrami Sandwich","Chicken Sandwich","Pastrami Sandwich","Egg Sandwich","Meatball Sandwich","Roast Beef Sandwich","Pastrami Sandwich","Grilled Chesse Sandwich"] 
finished_sandwiches = []
print("\nThe Deli has run out of pastrami")
while "Pastrami Sandwich" in sandwich_orders:
       sandwich_orders.remove("Pastrami Sandwich")
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"\nI made you a {sandwich}")
    finished_sandwiches.append(sandwich)

print("\nHere is a list of made sandwiches")
for made_sandwich in finished_sandwiches:
    print(f"\n  {made_sandwich}")           

#7.10
Dream_vacation = {}
response = True

while response:
    individual = input("\n Enter your name: ")
    fav_vacation = input("\n If you could visit one place in the world, where would you go? ")
    Dream_vacation[individual] = fav_vacation

    ask_again = input("\nWould you like answer again (yes/no): ")
    if ask_again == 'no':
        response = False

for person,vacation in Dream_vacation.items():
    print(f"\n  {person}'s dream vacation is {vacation}") 


 # Just decided to have fun with Nigeria's 2023 Election ! ! ! !   HA HA HA 🤪🤪🤪🤪🤪🤪🤪😁

election_polls = {}
polls = True

while polls:
    citizen_name = input("\nEnter your name: ")
    citizen_candidate = input("\nEnter your favorite candidate for the upcoming election: ")
    election_polls[citizen_name] = citizen_candidate

    continue_polls = input("\nWould you like to continue (yes/no): ")
    if continue_polls == 'no':
        polls = False

print("\nHere are opinions of the people so far")
for citizen,candidate in election_polls.items():
    print(f"\n   {citizen} : {candidate}")