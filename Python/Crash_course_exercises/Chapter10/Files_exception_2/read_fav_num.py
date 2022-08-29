#Exercise 10.11
from fileinput import filename
import json

filename = "num.json"
with open(filename) as f:
   num =  json.load(f)

print(f"I know your favourite number! It's {num}")   