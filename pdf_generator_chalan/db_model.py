import sqlite3


class db_model:
    def __init__(self):
        self.con = sqlite3.connect("chalan.db")
        self.cur = self.con.cursor()
    
    def dictfetchall(self):
        columns =[col[0] for col in self.cur.description]
        return [dict(zip(columns,row))
                   for row in self.cur.fetchall()]
    def create_table(self):
        self.cur.execute("create table vehicle(id, vehicle_image_path, number_plate_path, OCR, DATE_time, vehicle_class, voilation)")
        self.con.commit()

    def insert_data(self):
        id =797
        vehicle_image_path = r"C:\Users\hp\Downloads\Vinayan_New\pdf_generator_chalan\vehicle_img.jpg"
        number_plate_path = r"C:\Users\hp\Downloads\Vinayan_New\pdf_generator_chalan\num_plate.jpg"
        OCR ="WB06F5977"
        DATE_time = "22|06|2024 13:43:00:00"
        vehicle_class = "Car"
        voilation ="Overspeeding"
        self.cur.execute("insert into vehicle values (?,?,?,?,?,?,?)",(id, vehicle_image_path, number_plate_path, OCR, DATE_time, vehicle_class, voilation))
        self.con.commit()

    def get_data(self):
        self.cur.execute("select * from vehicle")
        data = self.dictfetchall()
        return data
    
    def delete_data(self):
        self.cur.execute("Delete from vehicle")
        self.con.commit()
    

obj = db_model()
# obj.create_table()
# obj.insert_data()
# obj.get_data()
# obj.delete_data()