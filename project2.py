#matka

import random

num = random.randint(1,10)
attempts = 1
counter = 3

print(num)

print("Game Started --- You have 3 guess remaining. ")

while attempts <= 3:
    matka = int(input("Enter a number: "))
    if matka == num:
        print("You won")
        break
    
    else:
        attempts = attempts + 1
        counter = counter - 1
        print("incorrect attempts", "Attempts left", counter)
