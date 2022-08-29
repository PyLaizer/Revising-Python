#Exercise 10.13


import json

def get_stored_username():
    """Get stored username if available"""
    filename = "username.json"
    try:
        with open(filename) as f:
            user_name = json.load(f)

    except FileNotFoundError:
       return None
    else:
        return user_name   

def get_new_username(x): 
    """Prompt for a new user""" 
    # user_name = input("Enter your username: ")
    filename = "username.json"
    with open(filename,"w") as f:
        json.dump(x,f)
    return x    


def greet_user():
    """Greets a user by name"""
    check_user = input("Enter your username: ")
    user_name = get_stored_username()
    
    if user_name == check_user:
        print(f"Welcome,back {user_name}")
    else:
        user_name = get_new_username(check_user)
        print(f"We'll remember you when you come back, {user_name}")

  
greet_user()                 


















   # filename = "username.json"
    # try:
    #     with open(filename) as f:
    #         user_name = json.load(f)

    # except FileNotFoundError:
    #     user_name = input("Enter your username: ")
    #     with open(filename,"w") as f:
    #         json.dump(user_name,f)
    #     print(f"We'll remember you when you come back, {user_name}") 

    # else:
    #     print(f"Welcome,back {user_name}")   
