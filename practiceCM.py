class ContactBook():
    def __init__(self):
        self.contacts = {}
        print("an object is created of type contactbook. ")
        print(self.contacts)
        
    def addContacts(self, k ,v):
        self.contact[k]= v
        print("Contact added sucessfully")
        
    def printContacts(self):
        print("contact list...")
        for k,v in self.contacts.items():
            print(k,v)
            
    
    def deleteContacts(self, k):
        if k in self.contacts:
            del self.contacts[k]
            print(k ,"Deleted sucessfully")
        else:
            print(k ,"Not found")
        
    def searchContacts(self, k):
        if k in self.contacts:
            print(self.contacts,[k])
        else:
            print(k ,"Not Found")
        
    def updateContacts(self,k,v):
        if k in self.contacts:
            self.contacts[k]=v
            print("Contact updated", [k])
        else:
            print(k ,"Not Found")
        
    
    
            

        
asad = ContactBook()
asad.addContacts("Faham", 9323754321)
asad.addContacts("Adi", 4874574233)
asad.printContacts()
asad.searchContacts("Max")
asad.updateContacts("Adi", 7021412345)
asad.deleteContacts("adi")
asad.printContacts()