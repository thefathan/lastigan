from tkinter import *
from PIL import ImageTk, Image  # pip install Pillow
import mysql.connector


#mySQL connector
mydb = mysql.connector.connect(
    host="tubesrpl.mysql.database.azure.com",
    user="fathan@tubesrpl",
    password="@Tubes555",
    database='upnormal'
    )
mycursor = mydb.cursor()


# convert from DB
mycursor.execute("SELECT * FROM statusmeja")
status = mycursor.fetchall()

#Update Database
def update_status_meja(no_meja:int, status_meja:str):
    if status_meja == "Terisi":
        mycursor.execute("UPDATE statusmeja SET status = 'Kosong' WHERE nomeja = {} ".format(no_meja))
        mydb.commit()
    elif status_meja == "Kosong":
        mycursor.execute("UPDATE statusmeja SET status = 'Terisi' WHERE nomeja = {} ".format(no_meja))
        mydb.commit()

#Update Labels
def update_label1():
    Label1.config(text="{}".format(status[0][1]))

def update_label2():
    Label2.config(text="{}".format(status[1][1]))

def update_label3():
    Label3.config(text="{}".format(status[2][1]))

def update_label4():
    Label4.config(text="{}".format(status[3][1]))

def update_label5():
    Label5.config(text="{}".format(status[4][1]))

def update_label6():
    Label6.config(text="{}".format(status[5][1]))

app = Tk()
app.title("Upnormal Map")
img =Image.open('logo2.jpg')
bg = ImageTk.PhotoImage(img)

app.geometry("500x500")

# Add image
labe90 = Label(app, image=bg)
labe90.place(x = 0,y = 0)

# Add text
label91 = Label(app, text = "Upnormal Map", font=("Times New Roman", 24))
label91.pack(pady = 50)

Label1 = Label(app, text="{}".format(status[0][1])).place(x=130, y=190)
Button1 = Button(app, width=3, bd=2, relief=GROOVE, command=lambda : [update_status_meja(1, status[0][1]), update_label1()]).place(x=135, y=222)
Label2 = Label(app, text="{}".format(status[1][1])).place(x=240, y=190)
Button2 = Button(app, width=3, bd=2, relief=GROOVE, command=lambda : [update_status_meja(2, status[1][1]), update_label2()]).place(x=245, y=222)
Label3 = Label(app, text="{}".format(status[2][1])).place(x=350, y=190)
Button3 = Button(app, width=3, bd=2, relief=GROOVE, command=lambda : [update_status_meja(3, status[2][1]), update_label3()]).place(x=355, y=222)

Label4 = Label(app, text="{}".format(status[3][1])).place(x=130, y=275)
Button4 = Button(app, width=3, bd=2, relief=GROOVE, command=lambda : [update_status_meja(4, status[3][1]), update_label4()]).place(x=135, y=310)
Label5 = Label(app, text="{}".format(status[4][1])).place(x=240, y=275)
Button3 = Button(app, width=3, bd=2, relief=GROOVE, command=lambda : [update_status_meja(5, status[4][1]), update_label5()]).place(x=245, y=310)
Label6 = Label(app, text="{}".format(status[5][1])).place(x=350, y=275)
Button3 = Button(app, width=3, bd=2, relief=GROOVE, command=lambda : [update_status_meja(6, status[5][1]), update_label6()]).place(x=355, y=310)


# Execute tkinter
app.mainloop()
