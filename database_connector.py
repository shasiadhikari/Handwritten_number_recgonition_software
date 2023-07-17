import sqlite3
from user import User
from new_user import NewUser

class LoginDatabase:
    conneection = sqlite3.connect("DataBase/login_database.db")
    cursor = conneection.cursor() 
    cursor.execute("CREATE TABLE IF NOT EXISTS user(username VARCHAR PRIMARY KEY, first_name VARCHAR, last_name VARCHAR, email VARCHAR, password VARCHAR);")
        

    @staticmethod
    def is_existing_user(user:User):
        user_name = user.get_user_name()
        user_passw = user.get_user_passw()
        cursor=LoginDatabase.cursor.execute("SELECT * FROM user WHERE username = '" + user_name +"'and password ='" + user_passw + "'")
        row = cursor.fetchone()
        return row
    
    @staticmethod
    def is_existing_user_name(user:User):
        user_name=user.get_user_name()
        cursor=LoginDatabase.cursor.execute("SELECT * FROM user WHERE username = '" + user_name + "'")
        row = cursor.fetchone()
        return row
    
    @staticmethod
    def upload_data(new_user:NewUser):
        dict=new_user.get_user_data()
        LoginDatabase.cursor.execute("INSERT INTO user (username, first_name, last_name, email, password)VALUES ('"+ 
                                                     dict["user_name"] +"','"+ 
                                                     dict["first_name"] +"','"+ 
                                                     dict["last_name"] +"','"+ 
                                                     dict["email"] +"','"+ 
                                                     dict["password"] +"' )")
        LoginDatabase.conneection.commit()
        LoginDatabase.close_connection()

    @staticmethod
    def close_connection():
        LoginDatabase.conneection.close()