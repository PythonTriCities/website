from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def better_page():
    return render_template('better.html',
                           my_string="Python is fun!",
                           my_list=[0, 1, 2, 3, 4, 5])


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
