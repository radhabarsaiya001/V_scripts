import sqlite3
from cryptography.fernet import Fernet 
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64
from flask import jsonify

class database_model:
    def __init__(self):
        self.con = sqlite3.connect('user_authentication_v1.db')
        self.cur = self.con.cursor() 
        self.key =''
        self.f = ''
        data = self.get_data()
        if data is None:
        # if not data:
            self.secret_key_generation()
            self.insert_data()
            print("insert data successfully!")
        else:
            self.key = data[0]["secret_key"]
            self.f = Fernet(self.key)

    # *******************for encrypted data storing ***********
    def secret_key_generation(self):
        password = b"gully@boy"
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
            )
        self.key = base64.urlsafe_b64encode(kdf.derive(password))
        self.f = Fernet(self.key)

    def dictfetchall(self,cursor):
        columns =[col[0] for col in cursor.description]
        return [dict(zip(columns,row))
                   for row in cursor.fetchall()]
    
    def create_table(self):
        self.cur.execute("create table user(id, name, password, secret_key)")
        self.con.commit()

    def alter_table(self):
        self.cur.execute("alter table user add secret_key")
        self.con.commit()
    
    def drop_table(self):
        self.cur.execute("drop table user_db")
        self.con.commit()
    
    def delete_table(self):
        self.cur.execute("delete from user")
        self.con.commit()
    
    def insert_data(self): 
        id = 797
        user_name = self.f.encrypt(b'Admin')
        password = self.f.encrypt(b'vinayan@123')
        print(password)
        key = self.key
        self.cur.execute("Insert into user values(?,?,?,?)",(id,user_name,password,key))
        self.con.commit()
    
    def get_data(self):
        self.cur.execute("select * from user")
        data = self.dictfetchall(self.cur)
        if len(data) !=0:
            return data
        return None
    
    def update_password(self,pwd):
        try:
            encry_pwd = self.f.encrypt(str.encode(pwd)).decode()
            print(encry_pwd)
            test = self.cur.execute(f"update user set password = '{encry_pwd}'")
            self.con.commit()
            print("commited_successfully!!")
            # return encry_pwd,
        except Exception as e:
            return f"The error is: {str(e)}"
        
    
    
obj= database_model()
# obj.create_table()
# obj.insert_data()
# obj.drop_table()
# obj.get_data()
# obj.delete_table()
# obj.insert_data()
# obj.update_password('kos@123')