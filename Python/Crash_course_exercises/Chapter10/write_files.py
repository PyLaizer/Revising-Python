#Exercise 10.3
user_input = input("Enter your name: ")
filename = 'guest.txt'
with open(filename,'w') as file_object:
    file_object.write(user_input)
  

#Exercise 10.4
filename = 'guest_book.txt'
active = 1
while active:
    print("\nType 'no' to STOP program ! ! ! ")
    user_name = input("Enter your name: ")
    if user_name == 'no':
        active = 0
    else:
       print(f"\nWelcome {user_name}") 
       with open(filename,'a') as file_object:
        file_object.write(f"\n{user_name}")
         


# filename = 'programming.txt'
# with open(filename,'w') as file_object:
#     file_object.write("I love programming")

