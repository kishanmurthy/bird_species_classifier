import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import uuid
from datetime import datetime
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
from utils import process_file
from pipelines.classifiers import bird_classifer

app = Flask(__name__, static_folder='app', static_url_path="/app")

app.config["DEBUG"] = True
app.config['image_dir'] = "images/"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route("/predict", methods=['POST'])
def predict():
    data_file = request.files['bird']
    file_path = process_file(data_file,app.config['image_dir'], ALLOWED_EXTENSIONS)
    result = bird_classifer.classify(file_path)
    return jsonify(result)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file("index.html")

app.run()



