
#       E       X       C       E       P       T       I       O       N

#Exercise 10.6
print("\nEnter a number for the following input! ! !")
try:
    first_num = int(input("\nEnter a number: "))
    second_num = int(input("\nEnter a number: "))
    # first_num = int(first_num)
    # second_num = int(second_num)
except ValueError:
    print("\nYou did not enter a valid integer in at least one of the inputs! Please enter valid integers next time")    
else:
    total = first_num + second_num
    print(total)


#Exercise 10.7
# active = 1
# while active:
#     print("\nEnter a number for the following input! ! !")
#     try:
#         first_num = int(input("\nEnter a number: "))
#         second_num = int(input("\nEnter a number: "))
#         # first_num = int(first_num)
#         # second_num = int(second_num)
#     except ValueError:
#         print("\nYou did not enter a valid integer in at least one of the inputs! Please enter valid integers next time")    
#     else:
#         total = first_num + second_num
#         print(total)
#         active = 0


#Exercise 10.8  & Exercise 10.9
filenames = ["cats.txt","dogs.txt"]

for filename in filenames:
    try:
        with open(filename,'r') as file_object:
            content = file_object.read()
    except FileNotFoundError:
        pass
        # print("\nThe expected file is probaly missing.")
    else:
        print(content)        