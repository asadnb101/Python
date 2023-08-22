def addFriends():
    friends = []
    
    print("Enter name of 5 friends")
    for i in range(5):
        friends.append(input())
        
        
    return friends

print(addFriends())