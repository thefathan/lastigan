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
Label2 = Label(app, text="{}".format(status[1][1])).place(x=240, y=190)
Label3 = Label(app, text="{}".format(status[2][1])).place(x=350, y=190)

Label4 = Label(app, text="{}".format(status[3][1])).place(x=130, y=275)
Label5 = Label(app, text="{}".format(status[4][1])).place(x=240, y=275)
Label4 = Label(app, text="{}".format(status[5][1])).place(x=350, y=275)

# Execute tkinter
app.mainloop()