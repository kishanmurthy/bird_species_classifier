from app import app
from flask import render_template

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
    return app.send_static_file("static/index.html")
    #return render_template('index.html')
    #return send_from_directory(os.path.join(root_dir, 'static', 'js'), filename("app/template/index.html")
