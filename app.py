"""
NOTES:
    -Why the difference in the @app.route format? /site vs /site/
    -Where are the board post going? Main page or dedicated?
TODO:
    -Add link to homepage from the about page, project page, and members page
    -Add background picture or design for now
    -Add a sign-up button to a link on the homepage
    -Add a schedule/calendar to a link on the homepage
    -Add an announcement and updates area on homepage
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)

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

@app.route('/projects/')
def projects():
    return render_template('projects.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/members')
def members():
    return render_template('members.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

