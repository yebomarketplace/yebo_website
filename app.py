from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def hello_world():
    return render_template('YeboHomepage.html')

@app.route('/app')
def hello_photos():
    return render_template('YeboPhotoApp.html')
#integrate this to do the photos
hists = os.listdir('static/plots')
hists = ['plots/' + file for file in hists]
return render_template('report.html', hists = hists)
