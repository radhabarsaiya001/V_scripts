from mtcnn_ort import MTCNN
import cv2
import time
import os 
from numpy import asarray, expand_dims, load
from numpy import savez_compressed
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
import joblib
from keras_facenet import FaceNet
svc_model = joblib.load(r"C:\Users\hp\Downloads\Vinayan_New\Real Time Face Recognition using Kafka\optimized_face_model.pkl")
label_encoder = joblib.load(r"C:\Users\hp\Downloads\Vinayan_New\Real Time Face Recognition using Kafka\optimized_label_encoder.pkl")
model = FaceNet()
detector = MTCNN()
data = load(r"C:\Users\hp\Downloads\Vinayan_New\Real Time Face Recognition using Kafka\face_embeddings_wth_labels.npz")


def extract_multiple_faces(frame_path, required_size=(160, 160)):
    img = cv2.imread(frame_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)      #for higher accuracy of MTCNN model
    face_pstn_lst = detector.detect_faces(img)
    frame_face_arr = []
    for i in range(len(face_pstn_lst)):
        x,y,w,h = face_pstn_lst[i]['box']
        face_arr = img[y:y+h, x:x+w]
        face_arr = cv2.resize(face_arr,required_size)
        face_arr = asarray(face_arr)
        frame_face_arr.append(face_arr)
    frame_face_arr = asarray(frame_face_arr)
    return frame_face_arr

def extract_multiple_embaddings(frame_face_arr):
    frame_all_embedding = []
    for i in frame_face_arr:
        samples = expand_dims(i,axis=0)  
        yhat = model.embeddings(samples)
        frame_all_embedding.append(yhat[0])

    frame_all_embedding = asarray(frame_all_embedding)
    return frame_all_embedding

def model_testing_on_realtime_sample(model, frame_all_embedding):
    for i in frame_all_embedding:
        sample_embedding = expand_dims(i, axis=0)
        train_y_pred = model.predict(sample_embedding)
        predicted_class = label_encoder.inverse_transform(train_y_pred)
        cnt = 0
        for i in data['arr_1']:
            if i == predicted_class[0]:
                training_embedding = data['arr_0'][cnt][:]
                training_embedding = expand_dims(training_embedding, axis=0)  
                break
            cnt+=1
        similarity_score = cosine_similarity(training_embedding,sample_embedding)
        similarity_score = round(similarity_score[0][0] * 100,3)
        if similarity_score < 60 :
            predicted_class = 'Unknown'
            yield predicted_class, f"{similarity_score} %"
        else:
            yield predicted_class[0], f"{similarity_score} %"
    

# frame_path = r"C:\Users\hp\Downloads\Vinayan_New\Real Time Face Recognition using Kafka\testing_data\multiple_face_testing.jpeg"
frame_path = r"C:\Users\hp\Downloads\Vinayan_New\Real Time Face Recognition using Kafka\testing_data\radha_an.jpeg"
frame_face_arr = extract_multiple_faces(frame_path)
frame_all_embedding = extract_multiple_embaddings(frame_face_arr)
model_testing =model_testing_on_realtime_sample(svc_model, frame_all_embedding)
for i,j in model_testing:
    print(i, j)
