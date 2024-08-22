import sqlite3
class database_model:
    def __init__(self):
        self.con = sqlite3.connect("Face_Recognition_DataBase.db",check_same_thread=False)
        self.cur = self.con.cursor()
    
    def create_table(self):
        self.cur.execute("create table if not exists face_tb(id, name)")
        self.con.commit()
    
    def delete_table(self):
        self.cur.execute("delete from face_tb")
        self.con.commit()

    def drop_table(self):   # delete the table structure complete with data....
        self.cur.execute("Drop table face_tb")
        self.con.commit()
    def insert_data(self, id, name):
        self.cur.execute("Insert into face_tb values (?,?)",(id,name))
        self.con.commit()

    def get_data(self,id):
        self.cur.execute("select name from face_tb where id = ?", (id,))
        data = self.cur.fetchone()
        return data[0]

# obj = database_model()
# print(obj.get_data(23))

