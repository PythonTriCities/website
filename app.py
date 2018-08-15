
from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path='/static', static_folder='/static')

announcements = [{
                    'title':'First Announcement',
                    'date_posted':'11 July 2018',
                    'content':'First Announcement Posted for Testing'
                },
                {
                    'title':'Second Announcement',
                    'date_posted':'12 July 2018',
                    'content':'Second Announcement Posted.'
                }]


@app.route('/')
def index_page():
    return render_template('index.html', announcements=announcements)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/members')
def members():
    return render_template('members.html')

@app.route('/projects/')
def projects():
    return render_template('projects.html')

@app.route('/login')
def login_page():
    return render_template('login-page.html')
