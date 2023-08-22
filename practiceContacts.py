contacts = {"Asad":9768360808}

def addContacts(k,v):
    contacts[k]=v
    print(k, "contacts added sucessfully")
    
def searchContacts(k):
    if k in contacts:
        print(k, contacts[k])
    else:
        print(k ,"not found.")
        
def deleteContacts(k):
    if k in contacts:
        del contacts[k]
        print(k ,"contact deleted")
    else:
        print(k , "not found")
        
def updateContacts(k,v):
    if k in contacts:
        contacts[k]=v
        print(k , "updated")
    else:
        print(k , "not found")
        
def printContacts():
    print("Contact lists....")
    for k,v in contacts.items():
        print(k,v)
        
addContacts("Saad", 9920612345)
printContacts()
searchContacts("Max")
deleteContacts("Saad")
printContacts()
updateContacts("Asad", 7021539108)
printContacts()

        