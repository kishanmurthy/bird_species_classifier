from werkzeug.utils import secure_filename
from datetime import datetime
import uuid
import os
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def get_file_extension(file_name):
    return file_name.split(".")[-1].lower()

def get_guid_filename(extension):
    return f'{uuid.uuid4().hex}_{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.{extension}'

def save_file(data_file,image_dir_path,filename):
    filepath = os.path.join(image_dir_path,filename)
    data_file.save(filepath)

def process_file(data_file,image_dir_path, extensions):
    extension = get_file_extension(data_file.filename)
    if extension not in extensions:
        raise Exception("Invalid File Extension")
    file_name = get_guid_filename(extension)
    save_file(data_file,image_dir_path,file_name)
    return file_name