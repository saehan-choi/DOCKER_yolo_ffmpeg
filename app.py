#  -*- coding: utf-8 -*-
import os
import time
import datetime
# import requests
from compression_process import compression
from werkzeug.utils import redirect
from flask import Flask, request, jsonify, send_file, render_template


from PyTorch_YOLOv4.yolo import yolo
from FFmpeg.ffmpeg_ import ffmpeg_process

app = Flask(__name__)

@app.route('/holy_world', methods=['POST','GET']) #test api
def holy_world():
    param = request.get_json()
    print('maybe you cant get a signal..?')
    return jsonify(param)
    # return 'Hello, World!'

# @app.route('/echo_call/<param>', methods=['POST','GET']) #get echo api
# def get_echo_call(param):
#     print(f'you get a <{param}>')
#     return jsonify({"param": param})

# ubuntu
@app.route('/fileupload', methods=['post'])
def file_upload():
    files = request.files.getlist("file")
    print(f'file uploaded!!!!{files}')
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    os.makedirs('/test_final/%s' % now, exist_ok=True)
    os.makedirs(f'{now}/input_images', exist_ok=True)
    os.makedirs(f'{now}/output_images', exist_ok=True)
    print(now)

    for file in files:
        file.save(os.path.join('/test_final/%s' % now, file.filename))
    # ffempeg()
    # def yolo(original_files, prediction_files)
    ffmpeg_process(f'/test_final/{now}', f'{now}/input_images')
    # ffmpeg_process(f'{now}/input_images', f'{now}/output_images')
    yolo(f'/test_final/{now}', f'{now}/output_images')
    # yolo(f'{now}/input_images', f'{now}/output_images')
    # 이거 나중에 ffempeg 들어오면 {now}/input_images 에 저장되게 하니깐 {now}/input_images 이걸로 고치기
    compression(now)
    while True:
        if os.path.isfile('/test_final/%s/%s.zip' % (now, now)):
            return send_file(os.path.join('/test_final/%s/%s.zip' % (now, now)))




@app.route('/fileupload_QT/<now>', methods=['post'])
def file_upload_qt(now):
    files = request.files.getlist("file")
    # param = request.get_json()
    # 담에받을땐 일케도 받아보깅
    # print(param)

    print(f'file uploaded!!!!{files}')
    # now = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    # os.makedirs('/test_final/static/qt', exist_ok=True)
    os.makedirs(f'static/qt/{now}/input_images', exist_ok=True)
    os.makedirs(f'static/qt/{now}/output_images', exist_ok=True)

    for file in files:
        file.save(os.path.join(f'/test_final/static/qt/{now}' , file.filename))
    
    # ffempeg()
    # def yolo(original_files, prediction_files)
    ffmpeg_process(f'/test_final/static/qt/{now}', f'static/qt/{now}/input_images')
    # ffmpeg_process(f'{now}/input_images', f'{now}/output_images')
    yolo(f'/test_final/static/qt/{now}/', f'static/qt/{now}/output_images')
    # yolo(f'{now}/input_images', f'{now}/output_images')
    # 이거 나중에 ffempeg 들어오면 {now}/input_images 에 저장되게 하니깐 {now}/input_images 이걸로 고치기
    # compression(now)

    return redirect(f'https://www.naver.com')

@app.route('/fileupload_v', methods=['post'])
def file_upload_v():
    files = request.files.getlist("file")
    print(f'file uploaded!!!!{files}')
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    os.makedirs('/test_final/static/%s' % now, exist_ok=True)
    os.makedirs(f'static/{now}/input_images', exist_ok=True)
    os.makedirs(f'static/{now}/output_images', exist_ok=True)
    print(now)

    for file in files:
        file.save(os.path.join('/test_final/static/%s' % now, file.filename))
    
    # ffempeg()
    # def yolo(original_files, prediction_files)
    ffmpeg_process(f'/test_final/static/{now}', f'static/{now}/input_images')
    # ffmpeg_process(f'{now}/input_images', f'{now}/output_images')
    yolo(f'/test_final/static/{now}', f'static/{now}/output_images')
    # yolo(f'{now}/input_images', f'{now}/output_images')
    # 이거 나중에 ffempeg 들어오면 {now}/input_images 에 저장되게 하니깐 {now}/input_images 이걸로 고치기
    # compression(now)
    
    path_dir = f'/test_final/static/{now}/input_images'
    file_list = os.listdir(path_dir)
    count = len(file_list)

    return redirect(f'http://192.168.25.250:5000/altar_viewer/{now}/{count}')

    # 페이지 넣기

@app.route("/file/")
def file():
    return render_template("")


if __name__ == "__main__":
     app.run(host='0.0.0.0', port='5000', debug=True)

