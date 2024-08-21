import cv2
import numpy as np
from PIL import Image
import os

cur_path = os.getcwd()
path = os.path.join(cur_path,'DataSet') 
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(r'C:\Users\hp\Downloads\Vinayan_New\Face Recognition System\OpenCV-Face-Recognition\FaceDetection\Cascades\haarcascade_frontalface_default.xml')

def getImagesAndLabels(path):
    imagesPaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids =[]
    for imagePath in imagesPaths:
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img,'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids

        # PIL_img.show()

print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

dir_name = "Trainer"
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
recognizer.write('Trainer/trainer.yml')
print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))