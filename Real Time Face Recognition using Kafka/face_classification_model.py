from numpy import load
from sklearn.preprocessing import LabelEncoder, Normalizer
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
import joblib
import matplotlib.pyplot as plt

# Load the dataset
data = load('face_embeddings_wth_labels.npz')
train_x = data['arr_0']
train_y = data['arr_1']

# Normalize the input vectors (train_x)
# normalizer = Normalizer(norm='l2')
# train_x = normalizer.fit_transform(train_x)

# Encode the labels
label_encoder = LabelEncoder()
train_y = label_encoder.fit_transform(train_y)

# Create the SVC model
svc_model = SVC(kernel='linear', probability=True)
svc_model.fit(train_x, train_y)

# Predict on training data
train_y_pred = svc_model.predict(train_x)

# Evaluate accuracy
# accuracy = accuracy_score(train_y, train_y_pred)
# print(f"Training Accuracy: {accuracy:.2f}")

# Print classification report
# print(classification_report(train_y, train_y_pred))

# Display confusion matrix

# ConfusionMatrixDisplay.from_estimator(svc_model, train_x, train_y)
# plt.show()

# Save the optimized model and label encoder
joblib.dump(svc_model, 'optimized_face_model.pkl')
joblib.dump(label_encoder, 'optimized_label_encoder.pkl')
# joblib.dump(normalizer, 'normalizer.pkl')
