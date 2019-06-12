#Including this here so that I can recreate the calls
#instagram-scraper {username} -m 100 --comments --profile-metadata --media-metadata --include-location

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
        try:
            comment = item['edge_media_to_caption']['edges'][0]['node']['text']
        except:
            comment = "Null"
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
    directory = os.listdir('static/IGContent/')
    directory = [file for file in directory if not file.endswith('.log')]
    info = [create_dict(folder) for folder in directory]
    info = [item for sublist in info for item in sublist]
    return render_template('YeboPhotoApp.html', info = info)
