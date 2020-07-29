from flask import Flask, render_template, Response
import cv2
import numpy as np
import pyautogui

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    while True:
        SCREEN_SIZE = (1360, 768) #SCREEN_SIZE is your screen resolution
        img = pyautogui.screenshot()
        frame = np.array(img)
        #frame = cv2.resize(frame, (640, 320)) #resize frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        (flag, encodedImage) = cv2.imencode(".jpg", frame)

        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')

#Host IP will be Your IP
if __name__ == '__main__':
    app.run(host='192.168.43.117', debug=True)