from numpy import load
from sklearn.preprocessing import LabelEncoder, Normalizer
from sklearn.svm import SVC
import joblib
import matplotlib.pyplot as plt
from Face_Registration import extract_faces
from facenet_embedding_extraction import extract_embaddings
from numpy import expand_dims
data = load('face_embeddings_wth_labels.npz')
train_x = data['arr_0']
train_y = data['arr_1']


label_encoder = LabelEncoder()
train_y = label_encoder.fit_transform(train_y)

# # Create the SVC model

svc_model = SVC(kernel='linear', probability=True)
svc_model.fit(train_x, train_y)


# Save the optimized model and label encoder
# joblib.dump(svc_model, 'optimized_face_model.pkl')
# joblib.dump(label_encoder, 'optimized_label_encoder.pkl')