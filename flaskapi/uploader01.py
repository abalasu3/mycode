import os
from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/home/student/mycode/flaskapi/uploads/'
@app.route("/upload")
def upload():
  return render_template("upload.html")

@app.route("/uploader", methods = ["GET", "POST"])
def upload_file():
  if request.method == "GET":  # if method is a get (same as "/upload")
     return render_template("upload.html")
  if request.method == "POST":
     f = request.files["file"]
     f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
     #f.save(secure_filename(f.filename))
  return "file uploaded successfully"

@app.route("/downloader")
def download_file():
    for file in os.listdir('/home/student/mycode/flaskapi/uploads/'): 
        return file

if __name__ == "__main__":
   app.run(port = 5006)
