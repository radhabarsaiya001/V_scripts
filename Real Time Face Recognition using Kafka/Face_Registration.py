from mtcnn_ort import MTCNN
import cv2
import time
import os 
from numpy import asarray
from numpy import savez_compressed
import matplotlib.pyplot as plt
detector = MTCNN()

def extract_faces(frame_path, required_size=(160, 160)):
    img = cv2.imread(frame_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)      #for higher accuracy of MTCNN model
    face_pstn_lst = detector.detect_faces(img)
    x,y,w,h = face_pstn_lst[0]['box']
    face_arr = img[y:y+h, x:x+w]
    face_arr = cv2.resize(face_arr,required_size)
    face_arr = asarray(face_arr)
    return face_arr

def load_dataset(data_dir):
    faces = []
    labels = []
    if os.path.isdir(data_dir):
        lst = os.listdir(data_dir)    
    for i in lst:
        frame_path = os.path.join(data_dir, i)
        face = extract_faces(frame_path=frame_path)
        # plt.imshow(face)
        # plt.show()
        # time.sleep(2)
        faces.append(face)

        frame_name = os.path.basename(frame_path)
        label = frame_name.split('.')[0]
        # print(label)
        labels.append(label)    
    return asarray(faces), asarray(labels)


data_dir= r'C:\Users\hp\Downloads\Vinayan_New\Real Time Face Recognition using Kafka\Data'
faces, labels = load_dataset(data_dir=data_dir)

savez_compressed('training_data.npz',faces, labels)







# img = cv2.imread(r'C:\Users\hp\Downloads\Vinayan_New\Real Time Face Recognition using Kafka\Data\radha_vinayan.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# faces = detector.detect_faces(img)

# # Draw bounding boxes around detected faces
# for face in faces:
#     x, y, w, h = face['box']
#     img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#     img = img[y:y+h, x:x+w]
#     img = cv2.resize(img, (160,160))

# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

