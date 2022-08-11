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