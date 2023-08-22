contacts = {"Asad":7021539108}


def addContact(k,v):
    contacts[k]=v
    
    
def deleteContact(k):
    if k in contacts:
        del contacts[k]
        print(k, "deleted sucessfully.")
    else:
        print(k, "not found")
        

def updateContact(k,v):
    if k in contacts:
        contacts[k]= v
    else:
        print(k, "not found")
        
        
def search(k):
    if k in contacts:
        print(k, contacts[k])
    else:
        print(k, "not found")
        
        
def printContacts():
    print("contact list..")
    for k,v in contacts.items():
        print (k,v)
        

addContact("aiman", 3352184589)
printContacts()
search("Asad")
deleteContact ("aiman")
updateContact("Asad", 9768360808)

printContacts()
