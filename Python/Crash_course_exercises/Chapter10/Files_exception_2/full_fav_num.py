#Exercise 10.12
#Combination of both Exercises  in 10.11 using the try-except-else block
import json

filename = 'num.json'
try:
    with open(filename) as f:
        num = json.load(f)

except FileNotFoundError:
    num = input('Type your favorite number: ')
    with open(filename,'w') as f:
        json.dump(num,f) 

else:
    print(f"I know your favourite number! It's {num}")    

