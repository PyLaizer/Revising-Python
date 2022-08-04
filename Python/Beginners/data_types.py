#DATA TYPES
# Text type = str
# Number type = int, float, complex
# Sequence type = list, tuple, range
# Mapping type = dict
# Set type = set, frozenset
# Boolean type = bool
# None type = none

a = "a"
print(a,type(a))

b = 15
print(b,type(b))

c = 22.5
print(c,type(c))

d = 1j
print(d,type(d))

e = [1,2,3,4,5,"boy","girl"]
print(e,type(e))

f = (1,2,3,4,5,"boy","girl","baywatch")
print(f,type(f))

g = range(10)
print(g,type(g))

h = {
    "player":"Karim Benzema",
    "club":"Real Madrid",
    "no":"10"
}
print(h,type(h))

i = {1,2,3,4,5,"love","hate","gain"}
print(i,type(i))

j = frozenset({1,2,3,"Tommy","Angelo","Vito Scaletta"})
print(j,type(j))

k = True
print(k,type(k))

l = None
print(l,type(l))


#Setting a variable to a specific data type: Using the following constructors

# Using the following constructors to define specific data types is called C A S T I N G 

a1 = str("Balmain")
print(a1,type(a1))

b1 = int(10.03)
print(b1,type(b1))

c1 = float(10)
print(c1,type(c1))

d1 = complex(10)
print(d1,type(d1))

e1 = list(("loner","hater","child of God"))
print(e1,type(e1))

f1 = tuple((21,22,23,45,"marred","scared","urinate"))
print(f1,type(f1))

g1 = range(5)
print(g1,type(g1))

h1 = dict(player="Modric",club="Real Madrid",age=36)
print(h1,type(h1))

i1 = set((1,2,3,4))
print(i1,type(i1))

j1 = frozenset({1,2,3,4})
print(j1,type(j1))

k1 = bool(45)
print(k1,type(k1))

l1 = None
print(l1,type(l1))


#                           N U M B E R  D A T A T Y P E ! ! !


#int: could be a whole number positive or negative 
int1 = 34
int2 = -34
print(type(int1),type(int2))

#float: could be a decimal digit positive or negative or a scientific digit
float1 = 34.56
float2 = -34.52
print(type(float1),type(float2))

float3 = 34e3
print(float3,type(float3))

#complex: They are written with j as the imaginary part; They could also be positive or negative
complex1 = 5j
complex2 = -5j
complex3 = 3 + 2j
print(type(complex1),type(complex2),type(complex3)) 

#Note: 
# 1. Type Conversion between numbers can be done using number constructors: can be seen among the data type syntax above
# 2. You cannot convert Complex data type into another type

#Random Number
# An in-built module called random can be used to generate random numbers
import random
print(random.randrange(1,20))

