# Exercise 10.11
import json

fav_num = input("Type your favourite number: ")

filename = "num.json"
with open(filename,"w") as f:
    json.dump(fav_num,f)
