
from numpy import load
from numpy import asarray
from numpy import expand_dims
from numpy import savez_compressed
from numpy import reshape
from keras.models import load_model 

model_path = r"C:\Users\hp\Downloads\Vinayan_New\Real Time Face Recognition using Kafka\model\facenet_keras.h5"
model = load_model(model_path)
print(model)