from tkinter import *
from tkinter import messagebox

def save():
    msgbox("Save Record!!", "Record")

def keyup(e):   #Checks the validity of the Customer e-mail
    for x in range(len(custemail.get())):
        if custemail.get()[-1] == "0" and x > 1:
            at = True
        else:
            labelemail.config(text = "Bad e-mail")

        if x > 4 and custemail.get()[-4:] == ".com" and at == True:
            dotcom = True
        else:
            labelemail.config(text = "Bad e-mail")


        if at == True and dotcom == True:
            labelemail.config(text = "Good e-mail")


def msgbox(msg, titlebar):
    messagebox.showinfo(title = titlebar, message = msg)


window = Tk()    # The main GUI form
window.title("Sample Window")
window.geometry("550x400")
window.configure(bg = "orange")


label = Label(window, text = "Customer Registration System", width = 30, height = 1, bg = "yellow")
label.config(font=("Courier",10))
label.grid(column = 2, row = 1)


label = Label(window, text = "Customer ID:", width = 10, height = 1, bg = "yellow") # Customer ID label
label.grid(column = 1, row = 2) #Position of Customer ID label
cid = StringVar()
custid = Entry(window, textvariable = cid)   #Customer ID Textfield
custid.grid(column = 2, row = 2) #Position of Customer ID Textfield


label = Label(window, text = "Customer name:", width = 15, height = 1, bg = "yellow") #Customer name label
label.grid(column = 1, row = 3) #Position of Customer name label
label = Label(window, text = "Lastname, Firstname", width = 20, height = 1, bg = "yellow")  #Customer name label instruction
label.grid(column = 3, row = 3)
custname = Entry(window) #Customer name Textfield
custname.grid(column = 2, row = 3)


label = Label(window, text = "Customer E-mail:", width = 15, height = 1, bg = "yellow")  #Customer E-mail label
label.grid(column = 1, row = 4)
labelemail = Label(window, text = "[a-z] @ [a-z].com", width = 15, height = 1, bg = "yellow") #Customer E-mail label instruction
labelemail.grid(column = 3, row = 4)
custemail = Entry(window)  #Customer E-mail Textfield
custemail.grid(column = 2, row = 4)
custemail.bind("<KeyRelease>", keyup)


savebtn = Button(text = "Save", command = save)
savebtn.grid(column = 1, row = 5)


window.mainloop()  






                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
