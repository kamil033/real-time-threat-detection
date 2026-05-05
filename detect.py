import cv2
import numpy as np

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier('models/face_detector.xml')

# Dummy emotion labels (replace with model later)
EMOTIONS = ["Neutral", "Happy", "Sad", "Angry"]

def predict_emotion(face_img):
    # Placeholder logic
    return np.random.choice(EMOTIONS)

def detect_faces_and_emotions(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    detections = []

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        emotion = predict_emotion(face)

        detections.append((x, y, w, h, emotion))

    return detections
