#!/usr/bin/env python3

from email.mime import image
from flask import Flask, jsonify, request, make_response, send_file, flash, redirect
import flask_cors

import exec_ia as ia
import resize
from PIL import Image

def main():
    app.run(host="0.0.0.0", port=5000, debug=True)

app = Flask(__name__)
flask_cors.CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods = ['POST'])
def analyse():
    if request.method == "POST":
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        #Receive an image
        image = request.files['file']
        #Rezise image to 416x416
        name = "input.png"
        image.save(name)
        resize.resize(name)
        #Exec model on image
        ia.exec_yolov3()
        image = Image.open("tmp.png")
        image = image.resize((1024,768))
        image.save("tmp.png")


    return send_file("tmp.png", mimetype='image/png')

if __name__ == "__main__":
    main()