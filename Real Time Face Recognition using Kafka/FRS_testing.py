import joblib
from numpy import load
from numpy import expand_dims
from facenet_embedding_extraction import extract_embaddings
from sklearn.preprocessing import LabelEncoder, Normalizer
from face_classification_model import classifing_model
from Face_Registration import extract_faces
frs_model = joblib.load('optimized_face_model.pkl')
label_encoder = joblib.load('optimized_label_encoder.pkl')
data = load('face_embeddings_wth_labels.npz')
cnt = 0
def get_training_embaddeing(frame_path):
    global cnt
    sample_embedding, predicting_class = classifing_model(frame_path)
    for i in data['arr_1']:
        if i == predicting_class[0]:
            print(cnt)
            break
        cnt+=1
    return sample_embedding

frame_path = r"C:\Users\hp\Downloads\Vinayan_New\Real Time Face Recognition using Kafka\testing_data\unknown_2.jpeg"
sample_embedding = get_training_embaddeing(frame_path)

training_embedding = data['arr_0'][cnt][:]
print(training_embedding)


similarity check function