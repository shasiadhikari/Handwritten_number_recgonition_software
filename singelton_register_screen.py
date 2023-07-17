from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

from igui import IGui

class Singelton_Register_Screen(IGui):
    __instance = None

    def __new__(cls):
        if (cls.__instance == None):
            cls.__instance = \
            super(Singelton_Register_Screen,cls).__new__(cls)
            cls.__instance.create_widget()
            return cls.__instance
        
    def create_widget(self):
        ## create tkinter object and set properties
        self.register_screen = Tk()
        self.register_screen.title("Registration Window")
        self.register_screen.geometry("1200x750")
        self.register_screen.resizable(False, False)
        
        # Background image
        self.bgimage = ImageTk.PhotoImage(Image.open('Image/backround.png'))
        self.bgimage_label = Label(self.register_screen,image=self.bgimage)
        self.bgimage_label.image = self.bgimage
        self.bgimage_label.pack()

        # First Name
        self.firstname_label = Label(self.register_screen,font=("times new roman", 20), text='First Name')
        self.firstname_label.place(x=550, y=150, width=250, height=40)
        self.user_firstname = Entry(self.register_screen,font=("times new roman", 20), bg="lightgray")
        self.user_firstname.place(x=800, y=150, width=250, height=40)

        # Last Name
        self.lastname_label = Label(self.register_screen,font=("times new roman", 20), text='Last Name')
        self.lastname_label.place(x=550, y=200, width=250, height=40)
        self.user_lastname = Entry(self.register_screen,font=("times new roman", 20), bg="lightgray")
        self.user_lastname.place(x=800, y=200, width=250, height=40)

        # Username
        self.username_label = Label(self.register_screen,font=("times new roman", 20), text='Username')
        self.username_label.place(x=550, y=250, width=250, height=40)
        self.username_entry = Entry(self.register_screen,font=("times new roman", 20), bg="lightgray")
        self.username_entry.place(x=800, y=250, width=250, height=40)

        # Email
        self.email_label = Label(self.register_screen,font=("times new roman", 20), text='Email')
        self.email_label.place(x=550, y=300, width=250, height=40)
        self.user_email = Entry(self.register_screen,font=("times new roman", 20), bg="lightgray")
        self.user_email.place(x=800, y=300, width=250, height=40)

        # Password
        self.passw_label = Label(self.register_screen,font=("times new roman", 20), text='Password')
        self.passw_label.place(x=550, y=350, width=250, height=40)
        self.user_passw = Entry(self.register_screen,font=("times new roman", 20), bg="lightgray")
        self.user_passw.place(x=800, y=350, width=250, height=40)

        # Confirm Password
        self.conpassw_label = Label(self.register_screen,font=("times new roman", 20), text='Confirm Password')
        self.conpassw_label.place(x=550, y=400, width=250, height=40)
        self.user_conpassw = Entry(self.register_screen,font=("times new roman", 20), bg="lightgray")
        self.user_conpassw.place(x=800, y=400, width=250, height=40)

        # Register button
        self.register_btn = Button(self.register_screen,text="Register",
                                   font=("times new roman", 15), bg="lightblue", bd=2, width=12, height=2)
        self.register_btn.place(x=850, y=550)

