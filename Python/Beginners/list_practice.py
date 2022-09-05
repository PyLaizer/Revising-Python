#       L  I   S   T

# Adding List items
class CarClass:
    """A list of cars"""
    def __init__(self,carlist):
        self.carlist = carlist

    def show_carlist(self):
        return self.carlist

    def append_carlist(self,item):
        self.carlist.append(item)   #  append() method
        return self.carlist

    def insert_carlist(self,car):
        self.carlist.insert(2,car)  #   insert() method
        return self.carlist  

    def extend_carlist(self,cars):
        self.carlist.extend(cars)   #   extend() method
        return self.carlist    

cars = ["Toyota","Audi","Tesla"]
carInstance = CarClass(cars)

print(f"\n{carInstance.show_carlist()}")
print(f"\n{carInstance.append_carlist('Aston Martin')}")
print(f"\n{carInstance.insert_carlist('Ford')}")

cars2 = ("Mclauren","Ferrari","Lamborghini","Bugatti","Lotus")
print(f"\n{carInstance.extend_carlist(cars2)}")


#Removing List items
class SportPlayers:
    """A class of different Sport players"""
    def __init__(self,players):
        self.players = players

    def remove_player(self,player):
        self.players.remove(player)
        return self.players 

    def pop_player(self):
        self.players.pop() 
        return self.players  

    def clear_list(self):
        return self.players.clear()

sport_players = ["Ronaldo","Jordan","Woods","Lebron","Messi","Serena"]
player_instance = SportPlayers(sport_players)

print(f"\n{player_instance.remove_player('Woods')}")
print(f"\n{player_instance.pop_player()}")
print(f"\n{player_instance.clear_list()}")

#List stuff
states = ["Abia","Adamawa","Anambra","Benue","Borno","Delta","Ebonyi","Edo"]
states_with_e = []
for x in states:
    if 'e' in x:
        states_with_e.append(x)
    elif 'E' in x:
        states_with_e.append(x)   

print(states_with_e)
        

             
        




