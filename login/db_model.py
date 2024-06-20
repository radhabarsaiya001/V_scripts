import sqlite3
from cryptography.fernet import Fernet 
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64

class database_model:
    def __init__(self):
        self.con = sqlite3.connect('user_authentication_v1.db')
        self.cur = self.con.cursor() 
        # *************encryption ----key generation***********
        # password = b"gully@boy"
        # salt = os.urandom(16)
        # kdf = PBKDF2HMAC(
        #     algorithm=hashes.SHA256(),
        #     length=32,
        #     salt=salt,
        #     iterations=480000,
        #     )
        # self.key = base64.urlsafe_b64encode(kdf.derive(password))
        # # key = Fernet.generate_key()
        # self.f = Fernet(self.key)

    def dictfetchall(self,cursor):
        columns =[col[0] for col in cursor.description]
        return [dict(zip(columns,row))
                   for row in cursor.fetchall()]

    def user_db(self): 
        # ***************create table***************
        # cur.execute("create table user(id, name, password)")

        # **********insert encrypted values********
        # id = self.f.encrypt(b'797')
        # user_name = self.f.encrypt(b'Admin')
        # password = self.f.encrypt(b'vinayan@123')
        # key = self.key
        # self.cur.execute("Insert into user values(?,?,?,?)",(id,user_name,password,key))
        # self.con.commit()
        # res = cur.execute("select * from user")
        # *********************delete from table************
        # self.cur.execute("delete from user")
        # self.con.commit()
        # *******************alter table***********
        # self.cur.execute("alter table user add secret_key")
        # self.con.commit()
        # print(res.fetchone())
        self.cur.execute("select * from user")
        # *************************user defined fetchall in dictonary*********************
        data = self.dictfetchall(self.cur)
        # print(data)
        # password = self.f.decrypt(data[0]["password"])
        # secret_key= data[0]["secret_key"]
        self.con.close()


        return data
    
# obj= database_model()
# obj.user_db()