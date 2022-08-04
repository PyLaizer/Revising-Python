# Revision Begins

# Variables



x = 45
y = "Python"
x = "Py.ai"

print(x)
print(y)

# Casting : Specifying the data type of a variable

z = int(3)
print(z)
z = float(3)
print(z)
z = str(3)
print(z)

print(type(x))
print(type(y))
print(type(z))

# Variable casing: camelCase and PascalCase
myAge = 89
myHeight = 6.4
MyChurch = "DLCM"

a1,a2,a3 = "xy","xx",76
print(a1)
print(a3)

x1 = x2 = x3 = "James "
print(x1)
print(x2)
print(x3)

# Python Collection

#list
alist = [1,2,3,4,5.9,"lavina"]
print(alist)

#tuple
atuple = (1,2,3,4,5)
print(atuple)

#set
aset = {1,2,3,4,5}
print(aset)

#dictionary
adict = {
    "brand":"Hewlett Packard",
    "model":"HP Envy x360",
    "model_no":"dx1033"
}
print(adict)

#Outputing variables; outputing multiple variables
print(a1,a2,a3)
print(myAge + myHeight) # + serves as addition
print (x1 + x2) # + serves as concatenation

#Function

xx3 = "Hello"

def myfunc(x):
    xx3 = "Welcome "
    print(xx3 + x)

myfunc("Homie")

print(xx3)

#Using a global variable in a function ; Use the global keyword

xyx = "Suiiii"
def afunc():
    global xyx
    xyx = "Seeeee"
    print(xyx)

afunc()   

print(xyx)