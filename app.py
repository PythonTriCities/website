from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/members')
def members():
    return 'The members page'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
