print("welcome to AskPython quiz game")
answer = input("Are you ready (yes or no)  ")
score = 0 

if answer.lower() == "yes": 
    print("lets begin")
    
    answer = input("who is the prime miniter of india? ")
    if answer.lower() == "narendra modi":
        print("correct")
        score= score + 1
        print("Your current score is", score)
        
    else:
        print("incorrect")
        
    answer = input("What is the national capital of india? ")
    if answer.lower() == "delhi":
        print("correct")
        score= score + 1
        print("Your current score is", score)
        
    else:
        print("incorrect")
        
    answer = input("National animal? ")
    if answer.lower() == "tiger":
        print("correct")
        score= score + 1
        print("Your current score is", score)
        
    else:
        print("incorrect")
        
    answer = input("national bird? ")
    if answer.lower() == "peacock":
        print("correct")
        score= score + 1
        print("Your current score is", score)
    else:
        print("incorrect")
        
    answer = input("financial capital? ")
    if answer.lower() == "mumbai":
        print("correct")
        score= score + 1
        
    else:
        print("incorrect")
        
    print("Your Final score is", score)
    
else:
    print("alright next time...")
    