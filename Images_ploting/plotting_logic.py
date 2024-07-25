# import cv2
# from datetime import datetime
# img = r"C:\Users\hp\Downloads\Vinayan_New\Images_ploting\original_image.png"
# # rocord_id =167803
# # speed = '87km/h'
# # speed_zone = '70km/h'
# # distance = '457.89 M'
# # direction = "jlkj;j;"
# # veh_type = "CAR"
# # veh_no = "DL9087"
# # veh_ctg = "Private"
# # voilation = "Overspeeding"
# # operator_name ="Vinayan"
# # op_id = 6789
# # lat = 23.675699
# # long = 77.8795645
# img_read = cv2.imread(img)
# # overlay = img_read.copy()
# fontScale = 1
# color = (255, 0, 0)
# voilation_color = (0,0,255)                                                                                         
# thickness = 2
# # font = cv2.FONT_HERSHEY_SIMPLEX 
# font = cv2.FONT_HERSHEY_PLAIN
# # date_time= datetime.now()
# # date_time_format = date_time.strftime("%d-%m-%Y %H:%M")
# # # print(date_time_format)

# # cv2.putText(img_read, date_time_format, (950,40),font, fontScale, color, thickness)
# # cv2.putText(img_read, f"RECORD ID: {rocord_id}", (20,40),font, fontScale, color, thickness)
# # cv2.putText(img_read, f"SPEED:{speed}, SPEED ZONE: {speed_zone}", (20,70),font, fontScale, voilation_color, thickness)
# # cv2.putText(img_read, f"DISTANCE: {distance}, DIRECTION: {direction}", (20,100),font, fontScale, color, thickness)
# # cv2.putText(img_read, f"LAT.: {lat}, LONG.: {long}", (20,130),font, fontScale, color, thickness)
# # cv2.putText(img_read, f"VEHICLE TYPE: {veh_type} , VEHICLE NO.: {veh_no}", (20,650),font, fontScale, color, thickness)
# # cv2.putText(img_read, f"VEHICLE CATEGORY: {veh_ctg}, VIOLATIONS: {voilation} ", (20,680),font, fontScale, voilation_color, thickness)
# # cv2.putText(img_read, f"OPERATOR NAME: {operator_name}, OPERATOR ID: {op_id}", (20,710),font, fontScale, color, thickness)
# # # cv2.imshow("win",img_read)
# # # cv2.waitKey(0)
# # # cv2.destroyAllWindows()
# # cv2.imwrite("customize_img.png",img_read)
# # # 
# # # sp = img_read.shape
# # # print(sp)
# cns= cv2.copyMakeBorder(img_read,30,30,0,0,cv2.BORDER_CONSTANT)
# cv2.putText(cns, f"DISTANCE: direction", (20,25),font, fontScale, color, thickness)
# cv2.putText(cns, f"VEHICLE TYPE:  , VEHICLE NO:", (10,740),font, fontScale, color, thickness)
# cv2.putText(cns, f"VIOLATIONS"  , (10,770),font, fontScale, color, thickness)
# cv2.putText(cns, f"OPERATOR NAME: , OPERATOR DEPARTMENT: LOCATION:", (10,800),font, fontScale, color, thickness)
# cv2.rectangle(cns,(0,30),(1050,60), (0,0,255),-1) 
# alpha = 0.4
# bg_img = cv2.addWeighted(cns, alpha, cns,1- alpha,0, 0)  
# cv2.imwrite("new_ip.png",bg_img)





import cv2
from datetime import datetime
img = r"C:\Users\hp\Downloads\Vinayan_New\Images_ploting\original_image.png"
img_read = cv2.imread(img)
fontScale = 1
color = (255, 0, 0)
voilation_color = (0,0,255)                                                                                         
thickness = 2
font = cv2.FONT_HERSHEY_SIMPLEX
cns= cv2.copyMakeBorder(img_read,30,30,0,0,cv2.BORDER_CONSTANT)
cv2.putText(cns, f"VEHICLE TYPE:  , VEHICLE NO:", (10,740),font, fontScale, color, thickness)
cv2.putText(cns, f"DISTANCE: direction", (20,25),font, fontScale, color, thickness)
cv2.putText(cns, f"VEHICLE TYPE:  , VEHICLE NO:", (10,740),font, fontScale, color, thickness)
cv2.putText(cns, f"VIOLATIONS"  , (10,770),font, fontScale, color, thickness)
cv2.putText(cns, f"OPERATOR NAME: , OPERATOR DEPARTMENT: LOCATION:", (10,800),font, fontScale, color, thickness)
overlay = cns.copy()
cv2.rectangle(overlay,(0,700),(1050,730), (0,0,0),-1)
alpha = 0.9
bg_img = cv2.addWeighted(cns, alpha, overlay, 1 - alpha, 0)
cv2.imwrite("overlay.png",bg_img)




# import cv2
# import numpy as np
# from datetime import datetime

# # Load the image
# img_path = r"C:\Users\hp\Downloads\Vinayan_New\Images_ploting\original_image.png"
# img_read = cv2.imread(img_path)

# # Define text parameters
# fontScale = 1
# text_color = (255, 0, 0)  # Blue color for the text
# voilation_color = (0, 0, 255)  # Red color (not used in this snippet)
# thickness = 2
# font = cv2.FONT_HERSHEY_SIMPLEX

# # Create a copy of the image with a border
# cns = cv2.copyMakeBorder(img_read, 30, 30, 0, 0, cv2.BORDER_CONSTANT)

# # Define text and its position
# text = "VEHICLE TYPE:  , VEHICLE NO:"
# text_position = (10, 740)

# # Get text size to determine the rectangle size
# (text_width, text_height), _ = cv2.getTextSize(text, font, fontScale, thickness)

# # Draw a filled rectangle as a black overlay
# overlay_top_left = (text_position[0], text_position[1] - text_height)
# overlay_bottom_right = (text_position[0] + text_width, text_position[1] + 10)  # Add 10 pixels for padding
# cv2.rectangle(cns, overlay_top_left, overlay_bottom_right, (0, 0, 0), -1)  # -1 fills the rectangle with black color

# # Put the text on top of the black rectangle
# cv2.putText(cns, text, text_position, font, fontScale, text_color, thickness)

# # Save the resulting image
# cv2.imwrite("plot.png", cns)
