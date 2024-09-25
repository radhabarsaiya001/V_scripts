import cv2
import time
import os 
from numpy import asarray, load
from numpy import expand_dims
from numpy import savez_compressed
from Face_Registration import extract_faces
from keras_facenet import FaceNet
import  matplotlib.pyplot as plt
model = FaceNet()

def extract_embaddings(frame_arr):
    samples = expand_dims(frame_arr,axis=0)  
    yhat = model.embeddings(samples)
    return yhat[0]

data = load('training_data.npz')

face_embedding = []
face_labels=[]
for i in range(len(data['arr_0'])):
    # plt.imshow(data['arr_0'][i])
    # plt.show()
    # print(data['arr_1'][i])
    lx = extract_embaddings(data['arr_0'][i])
    face_embedding.append(lx)
    face_label = data['arr_1'][i]
    face_labels.append(face_label)

# print(face_embedding)

# savez_compressed('face_embeddings_wth_labels.npz',face_embedding, face_labels)