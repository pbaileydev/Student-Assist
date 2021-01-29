from tkinter import *
import mysql.connector
viewport = Tk()
viewport.title("StudentAssist")
message = Label(viewport,text="Enter a student here:")
name = Entry(viewport,width=20)
age = Entry(viewport,width=20)
message.grid(padx=100,pady=15)
name.grid(padx=100,pady=17)
age.grid(padx=100,pady=19)
mydb = mysql.connector.connect(
    host="localhost",
    user="...",
    password="...",
    database="Students"
    )
cursor = mydb.cursor()
cursor.execute("Create Database IF NOT EXISTS Students")
cursor.execute("Create Table IF NOT EXISTS StudentInfo(ID INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(255), AGE INT)")
print(mydb)
def submit():
    dataName = name.get()
    dataAge = age.get()
    sql = "Insert Into StudentInfo(NAME,AGE) VALUES(%s,%s)"
    vals = (dataName,dataAge)
    cursor.execute(sql,vals)
    mydb.commit()
    cursor.execute("Select * from StudentInfo")
    result = cursor.fetchall()
    i = 0
    for row in result:
        labelX = Label(viewport,text= row)
        labelX.grid(padx = 100, pady = 22+i)
        i += 1
enter = Button(viewport,text="Enter",command=submit)
enter.grid(padx=100,pady=21)
viewport.mainloop()
