class User:
    def __init__(self,user_name:str,password:str):
        self.user_name= user_name
        self.password= password

    def get_user_name(self):
        return self.user_name

    def get_user_passw(self):
        return self.password