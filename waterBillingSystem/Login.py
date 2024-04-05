
from tkinter import *
from tkinter import messagebox
import mysql.connector



login = Tk()
login.title("Login")
login.geometry("400x300+600+150")

label1 = Label(login, text="UserName")
label1.place(x=50 ,y=50)

entry1 = Entry(login)
entry1.place(x=150, y=50)

label2  = Label(login , text= "Password")
label2.place(x=50, y=100)

entry2 = Entry(login)
entry2.place(x=150, y=100)

def loginUser():
    userName = entry1.get();
    print(userName)
    password = entry2.get();
    print(password)
    try:
     connection = mysql.connector.connect(host="localhost", database="waterbillingsystem", user="root", password="")
     if(connection):
        print("database successfully established")
     query = "SELECT * FROM login WHERE UserName=%s AND UserPassword=%s"
     data = (userName, password)
     c = connection.cursor()
     c.execute(query, data)
     result=c.fetchone()
     print(result)
     if(result):
         messagebox.showinfo("Login Successful", "Welcome, " + userName + "!")

     else:
          login.destroy()


    except mysql.connector.Error as error:
     print("Mysql error is "+error)
     
    finally:
        if(connection.is_connected()):
            connection.close()
def demise():
   login.destroy()

button1 = Button (login , text="Login", command=loginUser)
button1.place(x=80, y=200)

button2 = Button(login ,  text="Demise", command=demise)
button2.place(x=200, y=200)


login.mainloop()