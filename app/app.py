from datetime import datetime
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# using sqlite for testing
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

# this class along with any others should be in seperate files
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(100), nullable=False) # obviously we will want to move this to another table
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

    

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


if __name__ == '__main__':
    app.run(debug=True)
