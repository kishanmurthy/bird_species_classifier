from app import app
from flask import  request, jsonify
from app.utils import process_file
from pipelines.classifiers import bird_classifer
from fastai.vision.core import PILImage  

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


@app.route("/predict", methods=['POST'])
def predict():
    data_image = request.files['bird']
    #file_path = process_file(data_image,app.config['image_dir'], ALLOWED_EXTENSIONS,False)
    image = PILImage.create(data_image)
    result = bird_classifer.classify(image)
    return result



