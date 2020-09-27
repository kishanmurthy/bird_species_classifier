from flask import Flask
import os
app = Flask(__name__, template_folder="template")

app.config['image_dir'] = "images/"

from app import api
from app import spa

port = int(os.environ.get('PORT', 33507))
app.run(host='0.0.0.0',port=port)

