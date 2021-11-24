from tkinter import *
from PIL import ImageTk, Image  # pip install Pillow
import mysql.connector
import tkinter as tk

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
    

def update(Label1):
    Label1.config(text="{}".format(status[0][1]))
    print("test")


def main():
    #mySQL connector
    app = tk.Tk()
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

    Label1 = Label(app, text="{}".format(status[0][1]))
    Label1.place(x=130, y=190)
    Label2 = Label(app, text="{}".format(status[1][1]))
    Label2.place(x=240, y=190)
    Label3 = Label(app, text="{}".format(status[2][1]))
    Label3.place(x=350, y=190)

    Label4 = Label(app, text="{}".format(status[3][1]))
    Label4.place(x=130, y=275)
    Label5 = Label(app, text="{}".format(status[4][1]))
    Label5.place(x=240, y=275)
    Label6 = Label(app, text="{}".format(status[5][1]))
    Label6.place(x=350, y=275)



    btn = Button(app, text = 'Refresh', bd = '5', command = update(Label1)).place(x=230, y=380)


    # Fungsi


    # Execute tkinter
    app.mainloop()



# def restart(app):
#         self.refresh()
#         self.controller.show_frame("StartPage")

# def refresh(self):
#         self.weight_entry.delete(0, "end")
#         self.text.delete("1.0", "end")       
main()

