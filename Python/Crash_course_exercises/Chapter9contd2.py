#Exercise 9.13
from random import randint,choice, random

class Die:
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):    
        return randint(1,self.sides)


mydie = Die() #Add argument: 10 for 10 sides AND argument: 20 for 20 sides
print(mydie.roll_die())
print(mydie.roll_die())
print(mydie.roll_die())
print(mydie.roll_die())
print(mydie.roll_die())
print(mydie.roll_die())
print(mydie.roll_die())
print(mydie.roll_die())
print(mydie.roll_die())
print(mydie.roll_die())

#Exercise 9.14
mylist = [12,34,56,11,57,89,42,32,21,76,"a","e","i","o","u"]
# first_up = choice(mylist)
# second_up = choice(mylist)
# third_up = choice(mylist)
# fourth_up = choice(mylist)
x = 4
print(f"\nAny ticket matching these four numbers of letters wins a prize:")
while x > 0:
    firstup = choice(mylist)
    print(firstup)
    x -= 1

#Exercise 9.15
my_ticket = []
firstup = [56,32,89,11]
active = 1
while active:
    x = randint(1,100)
    for first in firstup:
        if x != first:
            print(x)
            my_ticket.append(x)
        else:
            print(f"\nWe finally have our lucky number: {x}")
            my_ticket.append(x)
            y = len(my_ticket)
            print(f"\nThe loop had to run {y} times to get the winning ticket")
            active = 0
            break


