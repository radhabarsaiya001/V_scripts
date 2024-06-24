import cv2
import numpy as np
from db_model import db_model
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.lib.units import cm, inch

class process:
    def __init__(self):
        self.database = db_model()
        self.get_data = self.database.get_data()
        self.vehicle_image_path = self.get_data[0]["vehicle_image_path"]
        self.number_plate_path = self.get_data[0]["number_plate_path"]
    
    def img_process(self):
        img = cv2.imread(self.vehicle_image_path)
        img_num = cv2.imread(self.number_plate_path)
        resized_img = cv2.resize(img,(300,180))
        resized_num_plate = cv2.resize(img_num,(250,50))
        cv2.imwrite(self.vehicle_image_path,resized_img)
        cv2.imwrite(self.number_plate_path,resized_num_plate) 

    def db_data(self):
        return self.get_data
    
    def pdf_generate(self):
        columns = self.dict_keys()
        y_columns = 185
        x_columns = 15
        pdf = Canvas("chalan.pdf",pagesize=(5 * inch, 7 * inch))    #inch is use to convert in point multiple 72 for 1 inch to point, 1 inch =72 points in pdf.
        pdf.drawInlineImage(self.vehicle_image_path,35,320)
        pdf.drawInlineImage(self.number_plate_path,55,260)
        pdf.setFont("Courier-Bold",16)
        for i in range(3,len(columns)):
            pdf.drawString(x_columns,y_columns,columns[i])
            y_columns-=24

        pdf.setFont("Courier",16)
        values = self.dict_values()
        x_values = 145
        y_values = 185
        for i in range(3,len(values)):
            pdf.drawString(x_values,y_values,values[i])
            y_values-=24
        x_lst = [10,142,357]
        y_lst = [200,176,152,128,104]
        pdf.grid(x_lst,y_lst)
        pdf.save()

    def dict_keys(self):
        data = self.get_data
        for i in data:
            keys = list(i.keys())
            return keys
    
    def dict_values(self):
        data = self.get_data
        for i in data:
            values = list(i.values())
            return values


obj = process()
# # obj.img_process()
# obj.db_data()
obj.pdf_generate()
# obj.dict_keys()
# obj.dict_values()
