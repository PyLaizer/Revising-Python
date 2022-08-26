#Exercise 10.5
filename = 'responses.txt'
active = 1
while active:
    print("\n Type 'no' to END program ! ! !")
    user_input = input("Why do you like programming: ")
    if user_input == 'no':
        active = 0
    else:
        print("\nThank you for your response.")
        with open(filename,'a') as file_object:
            file_object.write(f"\n{user_input}")

