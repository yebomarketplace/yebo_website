from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def hello_world():
    return render_template('YeboHomepage.html')
