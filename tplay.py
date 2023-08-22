import tkinter as tk

window= tk.Tk()
window.title("Visual")
window.geometry("1050x720")

l1= tk.Label(window,text="Python",foreground="white",background="black",font=('Times 30 bold')).grid(row=1,column=50)
l1= tk.Label(window,text="Name",foreground="black",background="white",font=('Times 14 bold')).grid(row=4,column=1)
def printSomthing():
    print("Hello")
    
b1=tk.Button(window,text="Click",command=printSomthing).grid(row=7,column=2)
r1=tk.Radiobutton(window,text="male",variable=None).grid(row=5,column=5)
textbox=tk.Entry(window).grid(row=4,column=3)

window.mainloop()