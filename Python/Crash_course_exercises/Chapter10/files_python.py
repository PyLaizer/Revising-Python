#Exercise 10.1
filename = 'learning_python.txt'

#Reads the entire file and prints it once
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

print()

#Loops over each line of the file and prints each line
with open(filename) as file_object:
    for line in file_object:
        print(line)

print()

#Stores the lines in a list, loops through the list and prints each line in the list
with open(filename) as file_object: 
    lines = file_object.readlines()     

for line in lines:
    print(line)  

print()
#Exercise 10.2
filename2 = 'learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        newLine = line.replace("Python","C")
        print(newLine)      

