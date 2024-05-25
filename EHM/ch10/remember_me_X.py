from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print("We will remember that!")
    return username
    


def get_stored_birthday(b):
    """Get em"""
    if b.exists():
        B = b.read_text()
        bd = json.loads(B)
        return bd
    else:
        return None
    
def get_new_birthday(b):
    bd = input("What's your birthday? (dd.mm.yyyy): ")
    B = json.dumps(bd)
    b.write_text(B)
    print("We will remember that!")
    return bd
    
    

def get_stored_city(c):


    if c.exists():
        CT = c.read_text()
        ct = json.dumps(CT)
        return ct
    else:
        return None

def get_new_city(c):
    """get their ip"""
    ct = input("What city are you from? ")
    CT = json.dumps(ct)
    c.write_text(CT)
    print("We will remember that!")
    return ct
    




def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    b = Path("Birthday.json")
    c = Path("city.json")
    Info = {}
    username = get_stored_username(path)
    bd = get_stored_birthday(b)
    ct = get_stored_city(c)
    
    if username and bd and ct:
        X = input(f"Is {username} correct username? (yes/no)") 
        if X == 'yes':
            print(f'Hello {username}, born in {bd}, from {ct}')
            Info['Username'] = username 
            Info['Birthday'] = bd
            Info['City'] = ct
        else:
            username = get_new_username(path)
            bd = get_new_birthday(b)
            ct = get_new_city(c)
    else:
        if username:
            Info['Username'] = username 
        else:
            username = get_new_username(path)
            Info['Username'] = username
        if bd:
            Info['Birthday'] = bd
        else: 
            bd = get_new_birthday(b)
            Info['Birthday'] = bd
        if ct:
            Info['City'] = ct
        else:
            ct = get_new_city(c)
            Info['City'] = ct
    
    
 
greet_user()