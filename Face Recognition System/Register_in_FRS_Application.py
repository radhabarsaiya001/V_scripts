import cv2
import os
import time
from Database import database_model

db = database_model()
db.create_table()
# db.delete_table()
def id_validation(dir_name):
    try:
        emty = []
        face_id = input("Enter user id: ")
        name = input("Enter you Good Name:")
        if os.path.exists(dir_name):
            existing_id= os.listdir(dir_name)

            for ids in existing_id:
                ids = ids.split('.')[1]
                emty.append(ids)
                emty = list(set(emty))
            # print("It's empty>>>>>>>>>>",emty)
            if face_id in emty:
                return str("The Id is registered, please you another ID !!")
            else:
                db.insert_data(face_id,name)
                return face_id
        else:
            return "DataSet Path is not Exist......"
    except Exception as e:
        return e

def register():
    dir_name = "DataSet"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        
    try:
        face_id = id_validation(dir_name)
        if face_id != "The Id is registered, please you another ID !!":
            print("Thanks for register in wonderful FRS Application!!")
            data_register(dir_name,face_id) 
        else :
            return "The Id is registered, please you another ID !!"
        # print(face_id)
    except Exception as e:
        return e
    
def data_register(dir_name, face_id):
    cam = cv2.VideoCapture(0)
    cam.set(3,640)
    cam.set(4,480)
    cnt = 0
    face_detector = cv2.CascadeClassifier(r'C:\Users\hp\Downloads\Vinayan_New\Face Recognition System\OpenCV-Face-Recognition\FaceDetection\Cascades\haarcascade_frontalface_default.xml')
    time_duration = 2
    required_frame = 10
    time_interval = time_duration/required_frame
    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    while(True):
        ret,img = cam.read()
        if not ret:
            pass
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            cnt+=1
            try:
                img_path = os.path.join(dir_name, f"User.{face_id}.{cnt}.jpg")
                cv2.imwrite(img_path, gray[y:y+h, x:x+w])
                print(f"[INFO] Image {cnt} saved at {img_path}")
                cv2.imshow('image', img)
                time.sleep(time_interval)
            except Exception as e:
                print(e)
        # cv2.imshow('image', img)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
        elif cnt>=10:
            break
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()

register()
# print(obj)

