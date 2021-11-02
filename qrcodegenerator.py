#Import the required Libraries
import qrcode
import datetime
from tkinter import *
from tkinter import ttk


#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x250")


#This is where the magic happens
def display_text():
    global entry
    string= entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )
    qr.add_data(string)
    qr.make(fit=True)

    img = qr.make_image(fill_color="red", back_color="white")
    img.save("url_qrcode_"+datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+".png")
    label.configure(text=string)

#Initialize a Label to display the User Input
label=Label(win, text="URL", font=("Courier 22 bold"))
label.pack()

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

#Create a Button to validate Entry Widget
ttk.Button(win, text= "Generate", width= 20, command= display_text).pack(pady=20)

win.mainloop()