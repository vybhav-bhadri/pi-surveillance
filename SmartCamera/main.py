from flask import Blueprint,render_template,Response
from . import db
from .camera import VideoCamera
import cv2
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

video_camera = VideoCamera(flip=True) # creates a camera object, flip vertically

def gen_vid(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@main.route('/')
@login_required
def index():
    return render_template('index.html',name=current_user.name)

@main.route('/video_feed')
def video_feed():
    return Response(gen_vid(video_camera),mimetype='multipart/x-mixed-replace; boundary=frame')


