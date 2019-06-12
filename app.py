from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def hello_world():
    return render_template('YeboHomepage.html')

@app.route('/app')
def hello_photos():
    photos = os.listdir('static/IGPosts')
    photos = ['IGPosts/' + file for file in photos]
    return render_template('YeboPhotoApp.html', photos = photos)
