import tkinter as tk

window=tk.Tk()

window.title("Visual Labs")
window.geometry("600x600")

l1= tk.Label(window,text="Python",foreground="black",background="blue",font=('Times 20 bold')).place(x=1,y=200)


l2= tk.Label(window,text="Name: ",foreground="black",font=('Times 14 bold')).grid(row=80,column=90)
textbox=tk.Entry(window).grid(row=80,column=150)

l3= tk.Label(window,text="Age: ",foreground="black",font=('Times 14 bold')).grid(row=140,column=90)
textbox=tk.Entry(window).grid(row=140,column=150)

l4= tk.Label(window,text="Gender: ",foreground="black",font=('Times 14 bold')).grid(row=200,column=90)
textbox=tk.Entry(window).grid(row=200,column=150)

b1=tk.Button(window,text="Submit").grid(row=350,column=50)



window.mainloop()