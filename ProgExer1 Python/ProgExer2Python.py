from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import *
from array import *
from time import *


at = False
dotcom = False

et = False



def save():
    msgbox("Save Record!!", "Record")

def keyup(e):   #Checks the validity of the Customer e-mail
    global at
    global dotcom
   
    for x in range(len(custemail.get())):
        if custemail.get()[-1] == "@" and x > 1:
            at = True
        else:
            labelemail.config(text = "Bad e-mail")
           
            

        if custemail.get()[-4:] == ".com" and x > 4 and at == True:
            dotcom = True
        else:
            labelemail.config(text = "Bad e-mail")
            


           
        if at == True and dotcom == True:
            labelemail.config(text = "Good e-mail")



def valDOB(date): #Checks the Bday Date Format
    bdayDate = custbday.get()
    format = "%m-%d-%Y"

    try:
        strptime(bdayDate, format)
        return True
    except ValueError:
        return False
    
    
    
    
    
    
    
    
    
    





def ageCalc(xAge):
    values = []
    for i in range(len(custbday.get())):
        values.append(custbday.get())
        
    values = xAge.split("/")
    month = int(values[0])
    day = int(values[1])
    year = int(values[2])

    today = date.today()
    years = today.year - year

    return years
    

    
    
    
    
    



def keybday(t):   #Checks the validity of the Customer Bday
    global et
    custbdayDate = custbday.get()

    isCorrect = valDOB(custbdayDate)


    for x in range(len(custbday.get())):

        if isCorrect == True and x > 9:
            et = True
            labelbday.config(text = "Good Date Format")
        else:
            labelbday.config(text = "Bad Date Format")


        if et == True:
            bop = custbday.get()
            calculatedAge = ageCalc(int(bop))

            if calculatedAge < 18:
                labelbday.config(text = "No Minors!")


        if len(custbday.get()) == 0:
             labelbday.config(text = "Empty Date input!")
            
                
            
            

        
            
    

    
    
    
    
    
    
    

       
            

        


def msgbox(msg, titlebar):
    messagebox.showinfo(title = titlebar, message = msg)


def products():
    window = Tk()
    window.title("Products Form")
    window.geometry("550x400")
    window.configure(bg = "orange")
    


window = Tk()    # The main GUI form
window.title("Sample Window")
window.geometry("550x400")
window.configure(bg = "orange")


menubar = Menu(window)   #Creates a MenuBar (upper left)
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu) #File menubar
filemenu.add_command(label = "Products", command = products)
filemenu.add_command(label = "Orders")
filemenu.add_separator()
filemenu.add_command(label = "Close", command = window.quit)

window.config(menu = menubar) #Activates the menu bar




label = Label(window, text = "Customer Registration System", width = 30, height = 1, bg = "yellow")
label.config(font=("Courier",10))
label.grid(column = 2, row = 1)


label = Label(window, text = "Customer ID:", width = 10, height = 1, bg = "yellow") # Customer ID label
label.grid(column = 1, row = 2) #Position of Customer ID label
cid = StringVar()
custid = Entry(window, textvariable = cid, state = 'disabled')   #Customer ID Textfield
custid.grid(column = 2, row = 2) #Position of Customer ID Textfield
cid.set("1")


label = Label(window, text = "Customer name:", width = 15, height = 1, bg = "yellow") #Customer name label
label.grid(column = 1, row = 3) #Position of Customer name label
labelname = Label(window, text = "Lastname, Firstname", width = 20, height = 1, bg = "yellow")  #Customer name label instruction
labelname.grid(column = 3, row = 3)
custname = Entry(window) #Customer name Textfield
custname.grid(column = 2, row = 3)


label = Label(window, text = "Customer Address:", width = 15, height = 1, bg = "yellow") #Customer Address label
label.grid(column = 1, row = 4)
custadrs = Entry(window)  #Customer Address Textfield
custadrs.grid(column = 2, row = 4)


label = Label(window, text = "Customer Contact #:", width = 16, height = 1, bg = "yellow") #Customer Contact # label
label.grid(column = 1, row = 5)
custcontact = Entry(window)  #Customer Contact # Textfield
custcontact.grid(column = 2, row = 5)


label = Label(window, text = "Customer E-mail:", width = 15, height = 1, bg = "yellow")  #Customer E-mail label
label.grid(column = 1, row = 6)
labelemail = Label(window, text = "[a-z] @ [a-z].com", width = 15, height = 1, bg = "yellow") #Customer E-mail label instruction
labelemail.grid(column = 3, row = 6)
custemail = Entry(window)  #Customer E-mail Textfield
custemail.grid(column = 2, row = 6)
custemail.bind("<KeyRelease>", keyup)


label = Label(window, text = "Customer Bday:", width = 15, height = 1, bg = "yellow")  #Customer Bday label
label.grid(column = 1, row = 7)
labelbday = Label(window, text = "mm/dd/yyyy", width = 15, height = 1, bg = "yellow") #Customer Bday label instruction
labelbday.grid(column = 3, row = 7)
custbday = Entry(window)  #Customer Bday Textfield
custbday.grid(column = 2, row = 7)
custbday.bind("<KeyRelease>", keybday)


label = Label(window, text = "Customer Gender", width = 15, height = 1, bg = "yellow") #Customer Gender label
label.grid(column = 1, row = 8)
custgender = ttk.Combobox(window, width = 8)  #Customer Gender Textfield
custgender['values'] = ("Male", "Female")
custgender.grid(column = 2, row = 8)









savebtn = Button(text = "Save", command = save)
savebtn.grid(column = 1, row = 9)


window.mainloop()  
