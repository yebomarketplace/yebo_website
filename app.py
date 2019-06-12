from flask import Flask
from flask import render_template
import os, glob, json

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def hello_world():
    return render_template('YeboHomepage.html')

@app.route('/app')
def hello_photos():
    photos = glob.glob('IGPosts/*.jpg')
    return render_template('YeboPhotoApp.html', photos = photos)
