
import cv2
import multiprocessing
from mtcnn_ort import MTCNN
from numpy import asarray, expand_dims
from sklearn.metrics.pairwise import cosine_similarity
import joblib
from keras_facenet import FaceNet
from numpy import asarray, expand_dims, load
import time

# Load pre-trained models
svc_model = joblib.load(r"C:\Users\hp\Downloads\Vinayan_New\Real Time Face Recognition using Kafka\model_pickel_files\optimized_face_model.pkl")
label_encoder = joblib.load(r"C:\Users\hp\Downloads\Vinayan_New\Real Time Face Recognition using Kafka\model_pickel_files\optimized_label_encoder.pkl")
model = FaceNet()
detector = MTCNN()
trained_faces = load(r"C:\Users\hp\Downloads\Vinayan_New\Real Time Face Recognition using Kafka\weight_model_files\face_embeddings_wth_labels.npz")


# Process a single frame for face detection
def detect_faces(frame_queue, embedding_queue):
    while True:
        frame = frame_queue.get()
        if frame is None:
            break

        # Detect faces using MTCNN
        faces = detector.detect_faces(frame)
        # frame_face_arr = []
        frame_face_positions = []

        # Process each face detected in the frame
        for face in faces:
            x, y, w, h = face['box']
            if face['confidence'] > 0.98:
                # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # face_arr = frame[y:y + h, x:x + w]
                # face_arr = cv2.resize(face_arr, (160, 160))
                # frame_face_arr.append(face_arr)
                frame_face_positions.append(face['box'])
        
        # if len(frame_face_arr) > 0:
        #     frame_face_arr = asarray(frame_face_arr)
        #     embedding_queue.put(frame_face_arr)
        if len(frame_face_positions) > 0:
            # frame_face_arr = asarray(frame_face_arr)
            embedding_queue.put((frame, frame_face_positions))
            # for frame_face_position in frame_face_positions:
            #     x, y, w, h = frame_face_position
            #     face_arr = frame[y:y + h, x:x + w]
            #     face_arr = cv2.resize(face_arr, (160, 160))
            #     frame_face_arr.append(face_arr)



# Capture frames from the RTSP stream
def capture_frames(rtsp_url, frame_queue):
    # cap = cv2.VideoCapture(rtsp_url)
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        if not frame_queue.full():
            frame_queue.put(frame)
    cap.release()

# Extract face embeddings using FaceNet
def extract_embeddings(embedding_queue, recognition_queue):
    while True:
        # frame_face_arr = embedding_queue.get()
        # if frame_face_arr is None:
        #     break

        data = embedding_queue.get()
        if data is None:
            break

        frame, face_positions = data
        frame_face_arr = []
        for frame_face_position in face_positions:
            x, y, w, h = frame_face_position
            face_arr = frame[y:y + h, x:x + w]
            face_arr = cv2.resize(face_arr, (160, 160))
            frame_face_arr.append(face_arr)

        frame_face_arr = asarray(frame_face_arr)
        frame_all_embedding = []

        for face in frame_face_arr:
            samples = expand_dims(face, axis=0)
            yhat = model.embeddings(samples)
            frame_all_embedding.append(yhat[0])
        if len(frame_all_embedding) > 0:
            recognition_queue.put((frame, face_positions,asarray(frame_all_embedding)))

# Perform classification and similarity checks on embeddings
def recognize_faces(recognition_queue):
    mapped_faces = []
    while True:
        # frame_all_embedding = recognition_queue.get()
        # if frame_all_embedding is None:
        #     break

        data = recognition_queue.get()
        if data is None:
            break

        frame, face_positions,frame_all_embeddings = data

        # for embedding in frame_all_embeddings:
        for idx, embedding in enumerate(frame_all_embeddings):
            sample_embedding = expand_dims(embedding, axis=0)
            predicted_class = svc_model.predict(sample_embedding)
            predicted_label = label_encoder.inverse_transform(predicted_class)[0]
            cnt = 0
            # print(trained_faces['arr_1'])
            for i in trained_faces['arr_1']:
                if i == predicted_label:
                    training_embedding = trained_faces['arr_0'][cnt][:]
                    training_embedding = expand_dims(training_embedding, axis=0)
                    break
                cnt += 1
            similarity_score = cosine_similarity(training_embedding, sample_embedding)
            similarity_score = round(similarity_score[0][0] * 100, 3)
            # if similarity_score < 60:
            #     print('Unknown', f"{similarity_score}%")
            # else:
            #     print(predicted_label, f"{similarity_score}%")
            if idx < len(face_positions):
                x, y, w, h = face_positions[idx]
                
                # Display or process the predicted label along with the face position
                if similarity_score < 60:
                    # print(f"Face at ({x}, {y}, {w}, {h}): Unknown - {similarity_score}%")
                    face_info = {
                    'position': (x, y, w, h),
                    'label': "Unknown",
                    'similarity_score': similarity_score
                        }
                    mapped_faces.append(face_info)

                else:
                    # print(f"Face at ({x}, {y}, {w}, {h}): {predicted_label} - {similarity_score}%")
                    face_info = {
                    'position': (x, y, w, h),
                    'label': predicted_label,
                    'similarity_score': similarity_score
                        }
                    mapped_faces.append(face_info)
                

                # Store the face position, label, and similarity score
                # face_info = {
                #     'position': (x, y, w, h),
                #     'label': predicted_label,
                #     'similarity_score': similarity_score
                # }
                
                # Append the face info to the mapped_faces list
                # mapped_faces.append(face_info)
        print(mapped_faces)
        return mapped_faces
    
    
# def recognize_faces(recognition_queue):
#     mapped_faces = []
    
#     while True:
#         data = recognition_queue.get()
#         if data is None:
#             break

#         frame, face_positions, frame_all_embeddings = data

#         # Cache trained embeddings for efficient lookup
#         trained_face_labels = trained_faces['arr_1']
#         trained_face_embeddings = trained_faces['arr_0']

#         for idx, embedding in enumerate(frame_all_embeddings):
#             sample_embedding = expand_dims(embedding, axis=0)
            
#             # Predict class using the SVC model
#             predicted_class = svc_model.predict(sample_embedding)
#             predicted_label = label_encoder.inverse_transform(predicted_class)[0]

#             # Efficiently find the matching label and corresponding embedding
#             if predicted_label in trained_face_labels:
#                 label_idx = trained_face_labels.tolist().index(predicted_label)
#                 training_embedding = trained_face_embeddings[label_idx]
#                 training_embedding = expand_dims(training_embedding, axis=0)
#             else:
#                 # If label not found in trained data, skip processing
#                 continue

#             # Calculate similarity score
#             similarity_score = cosine_similarity(training_embedding, sample_embedding)[0][0]
#             similarity_score = round(similarity_score * 100, 3)

#             # Handle face position and mapping
#             if idx < len(face_positions):
#                 x, y, w, h = face_positions[idx]
#                 face_info = {
#                     'position': (x, y, w, h),
#                     'label': predicted_label if similarity_score >= 60 else "Unknown",
#                     'similarity_score': similarity_score
#                 }
#                 mapped_faces.append(face_info)

#     print(mapped_faces)  # Optional: can be removed for production
#     return mapped_faces


# Main function to start the processes
def main():
    rtsp_url = "rtsp://admin:vinayan@123@192.168.1.64:554/1/1"

    # Create multiprocessing queues
    frame_queue = multiprocessing.Queue(maxsize=5)
    embedding_queue = multiprocessing.Queue(maxsize=5)
    recognition_queue = multiprocessing.Queue(maxsize=5)

    # Start the frame capture process
    capture_process = multiprocessing.Process(target=capture_frames, args=(rtsp_url, frame_queue))
    capture_process.start()

    # Start the face detection process
    detection_process = multiprocessing.Process(target=detect_faces, args=(frame_queue, embedding_queue))
    detection_process.start()

    # Start the face embedding extraction process
    embedding_process = multiprocessing.Process(target=extract_embeddings, args=(embedding_queue, recognition_queue))
    embedding_process.start()

    # Start the face recognition process
    recognition_process = multiprocessing.Process(target=recognize_faces, args=(recognition_queue,))
    recognition_process.start()

    # Wait for the processes to finish
    capture_process.join()
    frame_queue.put(None)  # Signal the processes to exit
    detection_process.join()
    embedding_queue.put(None)  # Signal the embedding process to exit
    embedding_process.join()
    recognition_queue.put(None)  # Signal the recognition process to exit
    recognition_process.join()

if __name__ == "__main__":
    main()