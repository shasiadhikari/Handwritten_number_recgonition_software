from user import User

class NewUser(User):
    def __init__(self,user_name:str,password:str,first_name:str,last_name:str,email:str,confirmed_password:str):
        super().__init__(user_name,password)
        self.first_name=first_name
        self.last_name = last_name
        self.email = email
        self.confirmed_password = confirmed_password

    def get_user_firstname(self):
        return self.first_name

    def get_user_lastname(self):
        return self.last_name

    def get_user_email(self):
        return self.email

    def get_confirmed_passw(self):
        return self.confirmed_password
    
    def get_user_data(self):
        return{
            'user_name': self.user_name,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'confirmed_password': self.confirmed_password
        }