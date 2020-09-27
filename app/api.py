from app import app
from flask import  request, jsonify
from app.utils import process_file
from pipelines.classifiers import bird_classifer

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


@app.route("/predict", methods=['POST'])
def predict():
    data_file = request.files['bird']
    file_path = process_file(data_file,app.config['image_dir'], ALLOWED_EXTENSIONS)
    result = bird_classifer.classify(file_path)
    return jsonify(result)



