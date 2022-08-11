

#                       L           I           S           T

# Exercise 3.1 - 3.3

#3.1



names = ["Magnus","Bartoz","Mikkel","Susan"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

#3.2
message_for_friend = "Hey, Hope you are feeling alright"
print(f"\n{names[0]} {message_for_friend}")
print(f"{names[1]} {message_for_friend}")
print(f"{names[2]} {message_for_friend}")
print(f"{names[3]} {message_for_friend}")

#3.3
fav_transport = ["Audi car","Mercedes Benz car","Aston Martin car","Ford car"]
print(f"\nI would like to own an {fav_transport[2]}")
print(f"I really like an {fav_transport[0]} and I would like to own one some day")
print(f"A {fav_transport[1]} is a strong vehicle")

#3.4
dinner = ["Mr Edward","Mrs Ann", "Mr Aniemeka"]
print(f"\n{dinner[0]}, you are invited to a dinner with Sir Eleazar. He would be most pleased to have you there")
print(f"{dinner[1]}, you are invited to a dinner with Sir Eleazar. He would be most pleased to have you there" )
print(f"{dinner[2]}, you are invited to a dinner with Sir Eleazar. He would be most pleased to have you there")

#3.5
print(dinner[0])
del dinner[0]
dinner.insert(0,"Mrs Udonwa")
print(f"\n{dinner[0]}, you are invited to a dinner with Sir Eleazar. He would be most pleased to have you there")
print(f"{dinner[1]}, you are invited to a dinner with Sir Eleazar. He would be most pleased to have you there" )
print(f"{dinner[2]}, you are invited to a dinner with Sir Eleazar. He would be most pleased to have you there")

#3.6
print(f"\nImportant Notice to {dinner[0]}, {dinner[1]}, {dinner[2]} : There will be a bigger dinner table")
dinner.insert(0,"Miss Laura")
dinner.insert(1,"Mrs Aniemeka")
dinner.append("Sir Elliot")

print(f"{dinner[0]}, you are invited to a dinner with Sir Eleazar. He would be most pleased to have you there")
print(f"{dinner[1]}, you are invited to a dinner with Sir Eleazar. He would be most pleased to have you there" )
print(f"{dinner[2]}, you are invited to a dinner with Sir Eleazar. He would be most pleased to have you there")
print(f"{dinner[3]}, you are invited to a dinner with Sir Eleazar. He would be most pleased to have you there")
print(f"{dinner[4]}, you are invited to a dinner with Sir Eleazar. He would be most pleased to have you there" )
print(f"{dinner[5]}, you are invited to a dinner with Sir Eleazar. He would be most pleased to have you there")

#3.9
no_of_guests = len(dinner)
print(f"\n{no_of_guests} guests were invited to my dinner")

#3.7
print("\nImportant Notice: We are really sorry but right now, there is only space for two guests")
popped1 = dinner.pop(0)
print(f"We are really sorry for the inconvenience {popped1} but your invitation to the dinner has been cancelled")
popped2 = dinner.pop(0)
print(f"We are really sorry for the inconvenience {popped2} but your invitation to the dinner has been cancelled")
popped3 = dinner.pop()
print(f"We are really sorry for the inconvenience {popped3} but your invitation to the dinner has been cancelled")
popped4 = dinner.pop(0)
print(f"We are really sorry for the inconvenience {popped4} but your invitation to the dinner has been cancelled")

print(f"\n{dinner[0]}, Congratulations, you are still invited to the dinner. Cheers !")
print(f"\n{dinner[1]}, Congratulations, you are still invited to the dinner. Cheers !")

#Having a wonderful dinner with these two. So ELITEEE!!!! Yipee
#What a wonderful dinner we had. Cheers to my guests. Adios amigos ! ! !
del dinner[0]
del dinner[0]
print(dinner)

#3.8
places = ["Germany","France","Dubai","United States","Canada"]
print(places)
print(sorted(places))

print(places)
print(sorted(places,reverse=True))

print(places)

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)

#3.10
lang1 = "German"
lang2 = "British English"
lang3 = "French"

langlist = []
langlist.append(lang1)
langlist.append(lang2)
langlist.append(lang3)
print(langlist)

print(sorted(langlist))

no_of_langs = len(langlist)
print(f"\n I would love to learn and speak at least {no_of_langs} languages in the world")

#3.11
tryList = ["Nielsen","Tiddermann","Kahnwald","Albas","Doppler","Tannhouse"]
print(tryList[5])
