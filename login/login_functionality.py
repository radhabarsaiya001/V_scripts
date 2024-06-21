from cryptography.fernet import Fernet 
from db_model import database_model
from flask import jsonify
class authentication():
    def __init__(self):
        pass
        # print(self.decrypt_pwd)

    def g_data(self):
        try:           
            self.database = database_model()        
            data = self.database.get_data()
            encry_name = data[0]["name"]
            encry_pwd = data[0]["password"]
            key = data[0]["secret_key"]
            self.f = Fernet(key)
            self.decrypt_name = self.f.decrypt(encry_name)
            self.decrypt_pwd = self.f.decrypt(encry_pwd)
            db_name = self.decrypt_name.decode()
            db_pwd = self.decrypt_pwd.decode()
            return db_name,db_pwd
        except Exception as e:
            return f"error: {e}"
       
    def update_data(self,new_pwd):
        try:
            self.database = database_model()        
            data = self.database.update_password(new_pwd)

        except Exception as e:
            return jsonify({'Error':str(e),'status':500})