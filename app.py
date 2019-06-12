from flask import Flask
from flask import render_template
import os, json

def create_dict(d_name):
    file = open('static/IGContent/'+d_name+'/'+d_name+'.json', encoding='utf-8')
    file = json.load(file)
    file = file["GraphImages"]
    d_info = []
    for item in file:
        url = os.path.basename(item['urls'][0]).split("?")[0]
        comment = item['edge_media_to_caption']['edges'][0]['node']['text']
        likes = str(item['edge_media_preview_like']['count'])
        username = item['username']
        d_info.append({
            'photo':'IGContent/'+d_name+'/'+url,
            'comment':comment,
            'likes':likes,
            'username':username
        })
    return d_info
    
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def hello_world():
    return render_template('YeboHomepage.html')

@app.route('/app')
def hello_photos():
    directory = 'yebomarketplace'
    info = create_dict(directory)
    return render_template('YeboPhotoApp.html', info = info)
