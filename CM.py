class ContactBook():
    def __init__(self):
        self.contacts = {}
        print ("Object created of type Contact book.")
        print (self.contacts)
        
    def addContacts(self, k, v):
        self.contacts[k]=v
        print("Contact added sucessfully.")
        
    def printContacts(self):
        print("contact list...")
        for k,v in self.contacts.items():
            print(k,v)
            
    def searchContacts(self,k):
        if k in self.contacts:
            print(self.contacts,[k])
        else:
            print("not found")
            
    def deleteContacts(self,k):
        if k in self.contacts:
            del self.contacts[k]
            print(k,"deleted sucessfully")
        else:
            print(k, "not found")
            
    def updateContacts(self,k,v):
        if k in self.contacts:
            self.contacts[k]= v
            print("Contacts updated", [k])
        else:
            print(k, "not found")
        
        
aiman = ContactBook()
aiman.addContacts("Asad", 9768360808)
aiman.addContacts("Saad", 9876543210)
aiman.printContacts()
aiman.searchContacts("Sam")
aiman.deleteContacts("Saad")
aiman.updateContacts("Asad", 70215369108)
aiman.printContacts()



mishaal = ContactBook()
mishaal.addContacts("Max", 5465415454)
mishaal.addContacts("Adi", 4874574233)
mishaal.printContacts()
mishaal.searchContacts("Jake")
mishaal.deleteContacts("Adi")
mishaal.updateContacts("Max", 70215369100)
mishaal.printContacts()