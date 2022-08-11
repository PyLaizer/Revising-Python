# Chapter 4 Exercises: For loop in list, List Comprehension, Slicing a list

#4.1
pizzas = ["Chicken Supreme","Chicken and Cheese","Chicken Pepperoni"]
for pizza in pizzas:
    print(f"I like {pizza}")
print(f"\nI like {pizzas[0]}")    
print(f"I like {pizzas[1]}")  
print(f"I like {pizzas[2]}")  
print("I really like pizza")

#4.2    
catFamily = ["Tiger","Lion","Jaguar","Cheetah","Puma"]
for animal in catFamily:
    print(f"A {animal} will make a great pet")
print("All these animals are within the Cat family.")    

#4.3
for x in range(1,21):
    print(x)

#4.4
#alist = list(range(1,1000000))
#for y in alist:
   # print(y)  

#4.5
# print(min(alist))
# print(max(alist))
# print(sum(alist))

#4.6
odd = list(range(1,20,2))
for y in odd:
    print(y)

#4.7
threes = list(range(3,30,3))
for num in threes:
    print(num)

#4.8
numList = []
cubes = range(1,11)
for num in cubes:
    numList.append(num**3)
for cube in numList:
    print(cube)  

#4.9  Using List Comprehension
listComp = [ cube**3 for cube in range(1,11) ] 
print(listComp) 

#4.10 Copying a list, Using the code from line 51
print(f"The first three items in the list are:{listComp[:3]}")
print(f"The items from the middle of the list are:{listComp[4:7]}")
print(f"The last three item in the list are:{listComp[-3:]}")

#4.11: Using the code from line 4
friend_pizzas = pizzas[:]
pizzas.append("Mushroom Royale")
friend_pizzas.append("Beef Supreme")
print("\nMy Favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favourite pizzas are:")    
for pizza in friend_pizzas:
    print(pizza)    

#4.12
favFoods = ["Stir fry spaghetti","Jollof rice","Eba and egusi soup","Fried rice and fried chicken"]
myBuddyFavFoods = favFoods[:]
for food in favFoods:
    print(food.title())
for food in myBuddyFavFoods:
    print(food.capitalize())    



#                       T       U       P       L       E

#4.13
Buffet = ("Crispy chicken","Barbecue","Tacos","Sandwich","Pasta")
for food in Buffet:
    print(food)

#Buffet[1] = "Ice cream" DO NOT UNCOMMENT, It would yield an error
Buffet = ("Doughnuts","Barbecue","Tacos","Hamburger","Pasta")  
for food in Buffet:
    print(food)  
    