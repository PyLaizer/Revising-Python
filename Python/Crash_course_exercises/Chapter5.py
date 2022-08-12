# Chapter 5 Exercises : IF Statement

#5.1 : Conditional Test
bestPlayer = "Cristiano Ronaldo"
print("Is the best player = 'Cristiano Ronaldo'? I predict true")
print(bestPlayer == "Cristiano Ronaldo")

print("\nIs the best player = 'Lionel Messi' ? I predict false")
print(bestPlayer == "Lionel Messi")

bestStriker = "Karim Benzema"
print("\nIs the best striker = 'Karim Benzema' ? I predict true")
print(bestStriker == 'Karim Benzema')

print("\nIs the best striker = 'Kylian Mbappe' ? I predict false")
print(bestStriker == 'Kylian Mbappe')

bestGoalkeeper = "Thibait Cortoius"
print("\nIs the best goal keeper = 'Thibait Cortoius' ? I predict true")
print(bestGoalkeeper == 'Thibait Cortoius')

print("\nIs the best goal keeper = 'Keylor Navas' ? I predict false")
print(bestStriker == 'Keylor Navas')

bestDefender = "Sergio Ramos"
print("\nIs the best goal defender = 'Sergio Ramos' ? I predict true")
print(bestDefender == 'Sergio Ramos')

print("\nIs the best goal defender = 'Gerard Pique' ? I predict false")
print(bestDefender == 'Gerard Pique')

bestMidfilder = "Lionel Messi"
print("\nIs the best goal midfilder = 'Lionel Messi' ? I predict true")
print(bestMidfilder == 'Lionel Messi')

print("\nIs the best goal midfilder = 'Bruno Fernandes' ? I predict false")
print(bestMidfilder == 'Bruno Fernandes')

#5.2
boy = "James"
print(boy == "John")
print(boy == "James")

print(boy != "John")
print(boy != "James")

girl = "jennifer"
print(girl == "Jennifer")
print(girl == "Jennifer".lower())

lbj = 23
sc = 30
print(lbj > sc)
print(lbj >= sc)
print(lbj < sc)
print(lbj <= sc)
print(lbj == sc)
print(lbj != sc)

print(lbj < 30 and sc > 23)
print(lbj > 30 and sc > 23)

print(lbj < 30 or sc > 23)
print(lbj > 30 or sc > 23)

ages = [43, 22, 18, 16, 11, 9]
print(13 in ages)
print(13 not in ages)

#5.3
alien_color = "red"

if alien_color == "green":
    print("\nYou just earned 5 points player")

if alien_color == "red":
    print("\nYou just earned 3 points player")

#5.4
if alien_color == "green":
    print("Player 1 has earned 5 points")

if alien_color != "green":
    print("Player 1 has earned 10 points")

if alien_color == "green":
     print("\nPlayer 1 has earned 5 points")
else:
    print("\nPlayer 1 has earned 10 points")

#5.5
alien_color = "red"

if alien_color == "green":
    print("The player earned 5 points")
elif alien_color == "yellow":
    print("The player earned 10 points")
elif alien_color == "red":
    print("\nThe player earned 15 points")

alien_color = "green"

if alien_color == "green":
    print("The player earned 5 points")
elif alien_color == "yellow":
    print("The player earned 10 points")
elif alien_color == "red":
    print("\nThe player earned 15 points")

alien_color = "yellow" 

if alien_color == "green":
    print("The player earned 5 points")
elif alien_color == "yellow":
    print("The player earned 10 points")
elif alien_color == "red":
    print("\nThe player earned 15 points")

#5.6
age = 43

if age < 2:
    print("The person is a baby")
elif age <4:
    print("The person is a toddler") 
elif age < 13:
    print("The person is a kid")
elif age < 20:
    print("The person is a teenager")    
elif age  < 65:
    print("The person is an adult")
else:
    print("The person is an elder")               


#5.7
favorite_fruits = ["apple","pineapple","avocado"]

if "apple" in favorite_fruits:
    print(f"\nI really like {favorite_fruits[0]}")

if "orange" in favorite_fruits:
    print(f"I really like orange")

if "pineapple" in favorite_fruits:
    print(f"I really like {favorite_fruits[1]}")

if "grape" in favorite_fruits:
    print(f"I really like grape")

if "avocado" in favorite_fruits:
    print(f"I really like {favorite_fruits[2]}")


#5.8
userNames = ["Chizzy001","Grandpapi","admin","Lordofritzy","Laizer2143","Melodee","Hamoni","Norelle070"]
for username in userNames:
    if username == "admin":
        print(f"\nHello {username}, would you like to see a status report")
    else:
        print(f"\nHello {username}, thank you for logging in again")     



#5.9
userNames = []

if userNames:
    print("\nAt least one user is present here")
else:
    print("\nWe need to find some users")    

#5.10
current_users = ["Osticks","Briks","Dadii.Savag3🖤🐐","Mideh.Jordan🌹","DammyMure","Orshii"]
current_users = ["osticks","briks","dadii.savag3🖤🐐","mideh.jordan🌹","dammymure","orshii"]
new_users = ["EL Troy","Crook","DammyMure","Beeg Tee","Wales","malcom🤓","osticks"]

for new_user in new_users:
    if new_user in current_users:
        print(f"\n Sorry the username: '{new_user}' has been used. Please enter a new username")
    else:
        print(f"\n This username: '{new_user}' is available")    

#5.11
numList = list(range(1,10))
for num in numList:
    if num == 1:
        print(f"\n {num}st")
    elif num == 2:
        print(f"\n {num}nd")
    elif num == 3:
        print(f"\n {num}rd")
    else:
        print(f"\n {num}th")            