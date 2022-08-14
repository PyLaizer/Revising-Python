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
    "animal_type":"frogs",
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
    print(f"The {pets['animal_type']} is owned by {pet['Owner']}")