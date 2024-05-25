from random import randint
from random import choice

class Die:
    def __init__(self, sides = 10):
        """defines"""
        self.sides = sides
    def roll_dice(self):
        """the interesting part"""
        print(randint(1, self.sides))

die = Die()
die.roll_dice()

elements = ['a', 'b', 'c', 'd', 'e']
winner_element = []
my_ticket = [] 

W = ''
M = ''
counter = 0
flag = True
while flag:
    for n in range(0,1):
        winner_element.append(choice(elements))
        my_ticket.append(choice(elements))
    

    for w in winner_element:
        w = str(w)        
        W += w
        

    for m in my_ticket:
        m = str(m)
        M += m

    print(f"\n{W}")
    print(M)
    
    if W != M:
        counter += 1
    elif W == M:
        flag = False
    
print(f'It took you {counter} attempts to win')
    

