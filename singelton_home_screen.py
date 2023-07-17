from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from user import User
from database_connector import LoginDatabase

from igui import IGui


class Singelton_Homescreen(IGui):
    __instance = None

    def __new__(cls):
        if (cls.__instance==None):
            cls.__instance = \
                super(Singelton_Homescreen,cls).__new__(cls)
            cls.__instance.create_widget()
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
        self.username:str = Entry(self.home_screen, font=("times new roman", 20), bg="lightgray")
        self.username.place(x=800, y=250, width=250, height=40)
        
        # Password label and entry
        password_label = Label(self.home_screen, font=("times new roman", 20), text='Password')
        password_label.place(x=550, y=350, width=250, height=40)
        self.password:str = Entry(self.home_screen, font=("times new roman", 20), bg="lightgray") 
        
        self.password.config(show='*')
        self.password.place(x=800, y=350, width=250, height=40)

        # Login button
        login_btn = Button(self.home_screen, text="Login", command=self.login, font=("times new roman", 15),
                           bg="lightblue", bd=2, width=12, height=2)
        login_btn.place(x=850, y=450)

        # Register button
        register_btn = Button(self.home_screen, text="Register Here", 
                              font=("times new roman", 15), bg="lightblue", bd=2, width=12, height=2)
        register_btn.place(x=850, y=550)

    def get_username(self):
        return self.username.get()
    
    def get_password (self):
        return self.password.get()
    
    def create_user(self):
        user = User(self.get_username(),self.get_password())
        return user

    def printa(self):
        print(self.get_username())

    def check_empty_fields(self):
        user = self.create_user()
        if not user.get_user_name()  or not user.get_user_passw() :
            messagebox.showerror("Error","All fields are required.")
            return
        else:
            return True
    def check_valid_user(self):
        row = LoginDatabase.is_existing_user(self.create_user())
        if row is None:
            messagebox.showerror("Error", "Invalid username and password")
            return
        else:
            return True
    def login(self):
        try:
            if self.check_empty_fields() and self.check_valid_user():
                LoginDatabase.close_connection()
                
        except Exception as e:
            messagebox.showerror("Error", str(e))


   
        



 
if __name__ == "__main__":
    app = Singelton_Homescreen()
    app.home_screen.mainloop()