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
    # face_arr = extract_faces(frame_path)
    samples = expand_dims(frame_arr,axis=0)  
    yhat = model.embeddings(samples)
    return yhat[0]


data = load('training_data.npz')

face_embedding = []
face_labels=[]
for i in range(len(data['arr_0'])):
    lx = extract_embaddings(data['arr_0'][i])
    # print(lx[:])
    face_embedding.append(lx)
    face_label = data['arr_1'][i]
    # print(face_label)
    face_labels.append(face_label)

# for i in range(len(face_embedding)):
#     print(face_embedding[i][23:45])
#     print(face_labels[i])


savez_compressed('face_embeddings_wth_labels.npz',face_embedding, face_labels)
