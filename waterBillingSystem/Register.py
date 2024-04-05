from tkinter import *
from tkinter import messagebox
import mysql.connector
import Login


register=Tk();
register.title("Register")
register.resizable(False,False)
register.geometry("400x350+600+150")


label1 =Label(register, text="FirstName")
label1.place(x=50,y=30)

Entry1 = Entry(register)
Entry1.place(x=180 , y=30)

label2 = Label(register, text="LastName")
label2.place(x=50, y=80)

Entry2 = Entry(register)
Entry2.place(x=180, y=80)

label3 = Label(register, text="Acc Number")
label3.place(x=50 , y=130)

Entry3 = Entry(register)
Entry3.place(x=180, y=130)

label4 = Label(register, text="UserName")
label4.place(x=50, y=180)

Entry4 = Entry(register)
Entry4.place(x=180, y=180)

label5 = Label(register, text="Password")
label5.place(x=50, y=230)

Entry5 = Entry(register)
Entry5.place(x=180, y=230)


def Register():
    firstName = Entry1.get()
    lastName = Entry2.get()
    accNumber = Entry3.get()
    userName = Entry4.get()
    password = Entry5.get()

    try:
        connection = mysql.connector.connect(host="localhost", database="waterbillingsystem", user="root", password="")
        if(connection):
            print("Database connection is successfully established")
        else:
            print("Database connection is not successfully established")

        query= "INSERT INTO register(firstname, lastname, accnumber, username, password) VALUES (%s, %s, %s, %s, %s)"
        data = (firstName, lastName, accNumber, userName, password) 
        C=connection.cursor()
        C.execute(query, data)
        print("Data insertion is successfully confirmed")
        connection.commit()
        C.close()

    except  mysql.connector.Error as error:
        print("Something went wrong "+error)
    
    finally:
        if(connection.is_connected()):
            connection.close()

button1 = Button(register, text="Registration", command = Register)
button1.place(x=80, y=280)

button2 = Button(register, text="Demise")
button2.place(x=250, y=280)
register.mainloop()


