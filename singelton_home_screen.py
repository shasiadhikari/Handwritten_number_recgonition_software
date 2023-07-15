from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

from igui import IGui


class Singelton_Homescreen(IGui):
    __instance = None

    def __new__(cls):
        if (cls.__instance==None):
            cls.__instance = \
                super(Singelton_Homescreen,cls).__new__(cls)
        return cls.__instance
    
    def create_widget(self):
        ## create tkinter object and set properties
        self.home_screen = Tk()
        self.home_screen.title("Number Recognition System")
        self.home_screen.geometry("1200x750")
        self.home_screen.resizable(False, False)

        ## set backround ##
        bg_image = ImageTk.PhotoImage(Image.open('Image/backround.png'))
        bg_label = Label(self.home_screen, image=bg_image)
        bg_label.image = bg_image
        bg_label.pack()

        # Username label and entry
        username_label = Label(self.home_screen, font=("times new roman", 20), text='Username')
        username_label.place(x=550, y=250, width=250, height=40)
        self.username = Entry(self.home_screen, font=("times new roman", 20), bg="lightgray")
        self.username.place(x=800, y=250, width=250, height=40)
        
        # Password label and entry
        password_label = Label(self.home_screen, font=("times new roman", 20), text='Password')
        password_label.place(x=550, y=350, width=250, height=40)
        self.password = Entry(self.home_screen, font=("times new roman", 20), bg="lightgray")
        self.password.config(show='*')
        self.password.place(x=800, y=350, width=250, height=40)

        # Login button
        login_btn = Button(self.home_screen, text="Login", font=("times new roman", 15),
                           bg="lightblue", bd=2, width=12, height=2)
        login_btn.place(x=850, y=450)

        # Register button
        register_btn = Button(self.home_screen, text="Register Here", 
                              font=("times new roman", 15), bg="lightblue", bd=2, width=12, height=2)
        register_btn.place(x=850, y=550)

if __name__ == "__main__":
    hs = Singelton_Homescreen()
   
    hs.create_widget()
    hs.home_screen.mainloop()
 