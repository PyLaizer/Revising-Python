# Exercise 8: FUNCTIONS

#               F       U       N       C       T       I       O       N       S

#Exercise 8.1
def display_messages(username):
    print(f"\n {username} is learning about 'Functions' in this chapter")

display_messages("Moritz")    
display_messages("Lenny")
display_messages("Fritzi")
display_messages("Lisa")
display_messages("Dan")

#Exercise 8.2
def favorite_book(title):
    print(f"\nOne of my favorite books is {title}")

favorite_book("Oliver Twist")   
favorite_book("Last days in Forcados High School")
favorite_book("The Lost city of Atlantis") 

#Exercise 8.3
def make_shirt(size,text):
    """Info about the shirt"""
    print(f"\n{size} size t-shirt with a text of '{text}'")

#Using positional Arguments
make_shirt("Large","Eyes of Heaven")
make_shirt("Extra Large","God over everything")

#Using keyword Arguments
make_shirt(size="Small",text="Memphis Athletics Dept 1986")
make_shirt(text="Black Perspective",size="Medium")

#Exercise 8.4
def make_shirt(size="Large",text="I love Python"):
    print(f"\n{size} size long-sleeve shirt with a text of '{text}'")

make_shirt()  
make_shirt(size="Medium")
make_shirt(size="Small",text="I love Artificial Intelligence")  

#Exercise 8.5
def describe_city(city,country="Nigeria"):
    print(f"\n{city} is in {country}")

describe_city("Festac")
describe_city("Ajah")    
describe_city("Winden","Germany")

#Exercise 8.6
def city_country(city,country):
    place = f"\n'{city}, {country}'"
    return place.title()

place1 = city_country("Paris","France")
place2 = city_country("lONDON","England")
place3 = city_country("lagos","nigeria")  

print(place1)
print(place2)
print(place3)

#Exercise 8.7
def make_album(name,title,num=None):
    if num:
        music_album = {
            "artist_name":name,
            "album_title":title,
            "number_of_songs":num,
        }
        return music_album
    else:
        music_album = {
            "artist_name":name,
            "album_title":title,
        }   
        return music_album

#LOOOOL ! ! ! ! I couldn't get any album name at the moment so I decided to use song names.
album1 = make_album("Eminem","Not Afraid")   
album2 = make_album("Kendrick Lamar","All the stars")
album3 = make_album("Dua Lipa","No lie",12)     

print(album1)
print(album2)
print(album3)

#Exercise 8.8
active = True
while active:
    print("\n Enter 'no' to quit program")
    input_name = input("\nEnter the artist name: ")
    if input_name == "no":
        break
    input_album = input("\nEnter the album name: ")
    if input_album == "no":
        break
    input_num = input("\nEnter the number of songs: ")
    if input_num == "no":
        break
    input_num = int(input_num)
    album4 = make_album(input_name,input_album,input_num)
    print(album4)
    print("\nDo you want to continue????")
    cont = input("yes/no: ")
    if cont == "no":
        active = False

#Exercise 8.9
def show_messages(texts):
    for text in texts:
        text_messages = f"\nYou have a message: {text}"
        print(text_messages)

messages = ["Win a trip to Dubai for #5000","Enjoy your favorite tv shows","Your subscription has expired, pls recharge","Dial *665# to borrow airtime from MTN"]
show_messages(messages)

#Exercise 8.10
def send_messages(texts,new_text):
    while texts:
        text = texts.pop()
        t_message = f"\nYou have a new message: {text}"
        print(t_message)
        new_text.append(t_message)
  


messages = ["Win a trip to Dubai for #5000","Enjoy your favorite tv shows","Your subscription has expired, pls recharge","Dial *665# to borrow airtime from MTN"]
sent_messages = []    
send_messages(messages,sent_messages)

print(messages)
print(sent_messages)

#Exercise 8.11
#Extended code from exercise 8.10
send_messages(messages[:],sent_messages)
print(messages)
print(sent_messages)
