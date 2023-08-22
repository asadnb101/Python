class area():
    def find_area(self,a,b):
        if a!=None and b!= None:
            print("A and B are called by their values given by the users", a,b)
        elif a!=None:
            print("A ko value di gayi hai",a,b)
        elif b!=None:
            print("B ko value di gayi hai",a,b)
        else:
            print("dono values default hai,a,b")
            
            
obj1=area()
obj1.find_area()
obj1.find_area(10)
obj1.find_area(None,20)
obj1.find_area(10,20)