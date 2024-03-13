import cv2
from flask import Flask, Response

app = Flask(__name__)

def webcam_stream():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        _, img_encoded = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(img_encoded) + b'\r\n')

    cap.release()

@app.route('/')
def index():
    return Response(webcam_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
