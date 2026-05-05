from flask import Flask, Response
import cv2
from detect import detect_faces_and_emotions
from tracker import CentroidTracker
from alert import check_alert

app = Flask(__name__)

cap = cv2.VideoCapture(0)
tracker = CentroidTracker()

def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break

        detections = detect_faces_and_emotions(frame)
        objects = tracker.update(detections)

        alert_flag = check_alert(objects)

        for (objectID, data) in objects.items():
            (x, y, w, h, emotion) = data
            color = (0, 0, 255) if alert_flag else (0, 255, 0)

            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, f"ID {objectID}: {emotion}",
                        (x, y-10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, color, 2)

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
