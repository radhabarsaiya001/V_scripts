import cv2
import numpy as np
from datetime import datetime

def plot(img_path, record_id, speed, speed_zone, distance, direction, veh_type, veh_no, veh_ctg, voilation, operator_name, op_id, lat, long, col_b, col_g, col_r,loc):
    img_read = cv2.imread(img_path)
    fontScale = 0.8
    color = (col_b,col_g,col_r)                                                                                        
    thickness = 2
    font = cv2.FONT_HERSHEY_SIMPLEX 
    date_time= datetime.now()
    date_time_format = date_time.strftime("%d-%m-%Y %H:%M")  
    borderd_img = cv2.copyMakeBorder(img_read,30,30,0,0,borderType=cv2.BORDER_CONSTANT)
    cv2.putText(borderd_img, date_time_format, (1000,55),font, fontScale, color, thickness)
    cv2.putText(borderd_img, f"RECORD ID: {record_id}", (10,55),font, fontScale, color, thickness)
    cv2.putText(borderd_img, f"SPEED:{speed} (SPEED ZONE: {speed_zone})", (10,85),font, fontScale, color, thickness)
    cv2.putText(borderd_img, f"DISTANCE: {distance} | DIRECTION: {direction}", (700,85),font, fontScale, color, thickness)
    cv2.putText(borderd_img, f"LAT: {lat} | LONG: {long}", (420,55),font, fontScale, color, thickness)
    cv2.putText(borderd_img, f"VEHICLE TYPE: {veh_type} ({veh_ctg}) , VEHICLE NO: {veh_no}", (10,680),font, fontScale, color, thickness)
    cv2.putText(borderd_img, f"VIOLATIONS: {voilation} ", (10,710),font, fontScale, color, thickness)
    cv2.putText(borderd_img, f"OPERATOR NAME: {operator_name}, OPERATOR DEPARTMENT: {op_id}, LOCATION: {loc}", (10,740),font, fontScale, color, thickness)
    overlay = np.zeros_like(borderd_img)
    cv2.rectangle(overlay,(0,30),(1280,100), (255,255,255), -1)
    cv2.rectangle(overlay,(0,650),(1280,750), (255,255,255), -1)
    alpha = 0.9
    final = cv2.addWeighted(borderd_img,alpha,overlay,1-alpha,0 )
    # cv2.imwrite("plot_image.png",borderd_img)
    cv2.imwrite("plot_image_output.png",final)