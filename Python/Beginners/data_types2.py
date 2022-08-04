
#                       S T R I N G     D A T A T Y P E 
x = "string"
print(x,type(x))

#multiline string
a =  """The red ridding horse
carried the little girl back to 
her home at once"""

print(a,type(a))

#Accessing a striing: similar to accessing an Array
y = "Gooday Mate !"
print(y[7])

#looping through a string
z = "Whatsapp Rommies"
for x in z:
    print(x)

#String Length: using the len() function
x1 = len(z)
print(x1)

#Checking for a certain word/character in a string: using the in keyword
txt = "It's a very beautiful morning"
chk = "very" in txt
print(chk)

#Using the if conditional statement to print an output when true
#Checks if a character or string is present in the  variable
txt1 = "Timetric Solutions Limited"
if "Solutions" in txt1:
    print("The word is present")

#Check IF Not
#Checks if a certain phrase or character is NOT present in a string: Using the not in keyword
txt2 = "The lazy dog failed to catch the thief"
print("hate" not in txt2)     

txt3 = "Systemtech Solutions Limited"
if "crazy" not in txt3:
    print("Doesn't exit")

#String slicing: First index = 0
a1 = "Peter Piper picked a peck of pickled pepper"
print(a1[0:8]) # slicing from 0 to 7: doesnt include the last index   
print(a1[:4]) # slicing from the beginning without the 0 index
print(a1[4:]) # slicing form 4 index to the end without the last index

#Negative indexing
print(a1[-6:-2])

        #python in-built string methods

#   .upper() method returns the string in uppercase
q1 = "Merry Christmas Y'all"
print(q1.upper())

#   .lower() method returns the string in lowercase
q2 = "Happy New Year"
print(q2.lower())

#   Removing whitespace: using the .strip() method 
#removes whitespace only from beginning and end and not in-between
q3 = " Crazy little asians be tripping all day "
print(q3.strip())

#   Replacing a string with another string: using the .replace() method
q4 = "The country will rise some day"
print(q4.replace("The","I hope that the"))

# Spliting a string: using the .split() methtod
#Using the split method converts the string to a list
q5 = "a,b,c,d,e,f,g,h,i,j,k,l"
print(q5.split(","))

q6 = "H a u n t e d"
print(q6.split(" "))

