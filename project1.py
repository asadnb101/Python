# sink a ship

import random

shipls = []
for i in range(3):
    num = random.randint(1,10)
    shipls.append(num)
    
print (shipls)  
print(shipls[0])
print(shipls[1])
print(shipls[2])

attempts = 1
counter = 5
score = 0

print("Game Started --- You have 5 guess remaining. ")

while attempts <=5:
    ship = int(input("Enter a number: "))
    
    if ship == (shipls[0]):
        score = score + 1
        print("You found a ship! ")
        
    elif ship == (shipls[1]):
        print("You found a ship! ")
        
        
    elif ship == (shipls[2]):
        print("You found a ship")
        break
        
    
    else:
        attempts = attempts + 1
        counter = counter - 1
        print("incorrect attempts", "Attempts left", counter)






