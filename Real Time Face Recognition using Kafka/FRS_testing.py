import joblib
import numpy as np
from numpy import expand_dims
from facenet_embedding_extraction import extract_embaddings
from sklearn.preprocessing import LabelEncoder
from Face_Registration import extract_faces
frs_model = joblib.load('optimized_face_model.pkl')
label_encoder = joblib.load('optimized_label_encoder.pkl')

# frame_path = r"C:\Users\hp\Downloads\Vinayan_New\Real Time Face Recognition using Kafka\Data\elon_1.jpg"
# frame_path = r"C:\Users\hp\Downloads\Vinayan_New\Real Time Face Recognition using Kafka\Data\WhatsApp Image 2024-09-24 at 11.30.27.jpeg"
frame_path = r"C:\Users\hp\Downloads\Vinayan_New\Real Time Face Recognition using Kafka\Data\bezos.jpeg"
face_arr = extract_faces(frame_path)
face_embadding = extract_embaddings(face_arr)

samples = expand_dims(face_embadding, axis=0)
yhat_class = frs_model.predict(samples)
yhat_prob = frs_model.predict_proba(samples)
label_name = label_encoder.inverse_transform(yhat_class)
class_index = yhat_class[0]
class_probability = 100 - (yhat_prob[0,class_index] *100)
print(yhat_class)
print(yhat_prob)
print(label_name)
print(class_probability)