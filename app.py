from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path='/static')

announcements = [{
    'title': 'First Announcement',
    'date_posted': '11 July 2018',
    'content': 'First Announcement Posted for Testing'
},
    {
        'title': 'Second Announcement',
        'date_posted': '12 July 2018',
        'content': 'Second Announcement Posted.'
    }]


@app.route('/')
def index_page():
    #show announcements, most recent one first
    #db = get_db()
    #posts = db.execute(
    #    'SELECT p.id, title, body, created, author_id, username'
    #    'FROM post p JOIN user u ON p.author_id = u.id'
    #    'ORDER BY created DESC'
    #).fetchall()
    return render_template('index.html', announcements=announcements)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/hello/')
@app.route('/hello/<string:name>')
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
