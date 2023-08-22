import mysql.connector

from tkinter import *

root=Tk()
root.title("insert")
root.geometry("600x600")

def submit():
    name = nameV.get()
    phone = phoneV.get()
    age = ageV.get()
    gender= genderV.get()
    
    print(name,phone,age,gender)
    
    db = mysql.connector.connect(
        host ="localhost",
        user="root",
        password= "123456",
        database="labs"
    )

    query = db.cursor()
    sql = "INSERT INTO Info VALUES('"+name+"', '"+phone+"', '"+age+"', '"+gender+"')"
    query.execute(sql)
    db.commit()
    query.close()
    
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    ageEntry.delete(0,END)
    genderEntry.delete(0,END)
    

Label(text="Register",foreground="white",background="blue",font=('Times 30 bold')).place(x=220,y=1)

Label(text="Name: ",fg="black",bg="white",
    font=('Times 15 bold')).place(x=100,y=150),
Label(text="Phone: ",fg="black",bg="white",
    font=('Times 15 bold')).place(x=100,y=200),
Label(text="age: ",fg="black",bg="white",
    font=('Times 15 bold')).place(x=100,y=250),
Label(text="Gender: ",fg="black",bg="white",
    font=('Times 15 bold')).place(x=100,y=300),

nameV=StringVar()
phoneV=StringVar()
ageV=StringVar()
genderV=StringVar()

nameEntry=Entry(root,textvariable=nameV,width=30,bd=2,font=('Times 19'))
nameEntry.place(x=200,y=150)

phoneEntry=Entry(root,textvariable=phoneV,width=30,bd=2,font=('Times 19'))
phoneEntry.place(x=200,y=200)

ageEntry=Entry(root,textvariable=ageV,width=30,bd=2,font=('Times 19'))
ageEntry.place(x=200,y=250)

genderEntry=Entry(root,textvariable=genderV,width=30,bd=2,font=('Times 19'))
genderEntry.place(x=200,y=300)


Button(text="Submit",fg="Black",bg="White",font='Times 20',command=submit).place(x=250,y=380)
root.mainloop()