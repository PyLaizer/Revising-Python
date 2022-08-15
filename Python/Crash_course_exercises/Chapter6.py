#Exercise 6 : Dictionary

#           D           I       C       T       I       O       N       A       R       Y

#6.1
personDict = {
    "first_name":"Joseph",
    "last_name":"Nweke",
    "age":20,
    "city":"Ikorodu",
    }
print(personDict["first_name"])
print(personDict["last_name"])
print(personDict["age"])
print(personDict["city"])

#6.2
favouriteNumbers = {
    "Kyrie":2,
    "LeBron":23,
    "Durant":35,
    "Steph":30,
    "Jordan":23,
    }

kyrie = favouriteNumbers["Kyrie"]
print(f"Kyrie's favourite number is {kyrie}")

LeBron = favouriteNumbers["LeBron"]
print(f"LeBron's favourite number is {LeBron}")

Durant = favouriteNumbers["Durant"]
print(f"Durant's favourite number is {Durant}")

Steph = favouriteNumbers["Steph"]
print(f"Steph's favourite number is {Steph}")

Jordan = favouriteNumbers["Steph"]
print(f"Steph's favourite number is {Jordan}")

#6.3
glossary = {
    "immutable":"Something unabled to change",
    "slice":"a fraction of something",
    "keyword":"Reserved words that are set apart for specific purposes",
    "Operators":"Symbols that are used to perform specific operations",
    "None":"Not a value"
    }

print(f"\n'immutable': {glossary['immutable']} ")
print(f"\n'slice': {glossary['slice']} ")
print(f"\n'keyword': {glossary['keyword']} ")
print(f"\n'Operators': {glossary['Operators']} ")
print(f"\n'None': {glossary['None']} ")

#6.4 Using Line 42
for word,meaning in glossary.items():
    print(f"\n'{word}': {meaning}")

glossary["integer"] = "a whole number/ digit that doesn't have a decimal"  
glossary["float"] = "a digit that has a decimal"
glossary["list"] = "uses square-brackets"
glossary["tuple"] = "uses parenthesis"
glossary["set"] = "uses braces" 

for name,meaning in glossary.items():
    print(f"\n'{name}' : {meaning}")

#6.5
Rivers = {
    "nile":"Egypt",
    "zambezi":"Zimbabwe",
    "umgeni":"South Africa",
}
for river,location in Rivers.items():
    print(f"\n The {river.title()} runs through {location}")

for river in Rivers.keys():
    print(f"\n The {river.title()} river")

for location in Rivers.values():
    print(f"\n {location}, Africa")        

#6.6
favouriteLanguages = {
    "Iredia":"C",
    "Emma":"PHP",
    "Maro":"Python",
    "Tega":"Python",
    "Prosper":"Java",
}
people = ["Emma","Cornelius","Adams","Tega","Goodness","Prosper","Akhere","Dennis","Kingsley"]
for name in people:
    if name in favouriteLanguages.keys():
        print(f"\n{name}, thanks for responding.")
    else:
        print(f"\n{name}, please take part of the poll.")        

#6.7        
personDict1 = {
    "first_name":"Joseph",
    "last_name":"Nweke",
    "age":20,
    "city":"Ikorodu",
    }

personDict2 = {
    "first_name":"Nicholas",
    "last_name":"Awoyemi",
    "age":22,
    "city":"Yaba",
    }

personDict3 = {
    "first_name":"Uche",
    "last_name":"Okeke",
    "age":20,
    "city":"Yaba",
    }

people = [personDict1,personDict2,personDict3]         
for person in people:
    print(f"\nInformation about this user:")
    print(f"First name: {person['first_name']}")
    print(f"Last name:{person['last_name']}")  
    print(f"Age: {person['age']}")   
    print(f"City: {person['city']}") 

#6.8
pet1 = {
    "animal_type":"bird",
    "Owner":"Basil",
}          

pet2 = {
    "animal_type":"frog",
    "Owner":"Christene",
} 

pet3 = {
    "animal_type":"dog",
    "Owner":"Magnus",
} 

pet4 = {
    "animal_type":"cat",
    "Owner":"Linda",
} 

pets = [pet1,pet2,pet3,pet4]
for pet in pets:
    print(f"\nThe {pet['animal_type']} is owned by {pet['Owner']}")

#6.9
favorite_places = {
    "Chidubem":"Florida",
    "Awele":"London",
    "Elliot":"Paris",
}   

for child,fav_place in favorite_places.items():
    print(f"\n{child}'s favorite place to visit is {fav_place}")

#6.10
favouriteNumbers = {
    "Kyrie":[2,3,4],
    "LeBron":[23,24,25],
    "Durant":[35,36,37],
    "Steph":[30,31,32],
    "Jordan":[23,35],
    }

for player,fav_num in favouriteNumbers.items():
    print(f"\n{player}'s favotite numbers are: ")
    for num in fav_num:
        print(f"{num}") 

#6.11
cities = {
   "Florida":{
    "Country":"United States Of America",
    "Population":21_220_000,
    "Fact":"Florida has the most golf course than any state in America",
   },
   "London":{
    "Country":"United Kingdom",
    "Population":8_982_000,
    "Fact":"London is the smallest city in England",
   },
   "Paris":{
    "Country":"France",
    "Population":2_100_000,
    "Fact":"Paris has one of the most famous paintings in the world",
   }, 
} 
for city,info in cities.items():
    print(f"\nSome Info about {city}:")
    for data,result in info.items():
        print(f"'{data}': {result}")     

#6.12
#Using exercise 6.9
favorite_places["Mitchelle"] = "United States of America"
favorite_places["Laura"] = "Canada"

for child,fav_place in favorite_places.items():
    print(f"\n{child}'s favorite place to visit is {fav_place}")



#Just tested looping through a specific nested Dictionary! ! ! ! 
# 
# 
# 
# O M G, It Worked ! ! ! ! ! 😱😱😱😱😱😱😱😱😱😱🤪😊☺️
testdict = {
    "a":"ahhhhh",
    "b":"bahhhh",
    "c":{
        "Heat":"Miami",
        "Celtics":"Boston",
        "Lakers":"Los Angeles",
    },
}

for team,city in testdict["c"].items():
    print(f"\nThe '{team}' are representing {city}.")