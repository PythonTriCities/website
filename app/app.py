from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#app.config['SECRET_KEY'] = ''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.app_db'

app_db = SQLAlchemy(app)

# User class(table) for app_db
class User(app_db.Model):
    id = app_db.Column(app_db.Integer, primary_key=True)
    username = app_db.Column(app_db.String(20), unique=True, nullable=False)
    email = app_db.Column(app_db.String(50), unique=True, nullable=False)
    image_file = app_db.Column(app_db.String(20),
                           nullable=False,
                           default='default.jpg')
    # obviously we will want to move this to another table
    password = app_db.Column(app_db.String(100), nullable=False)
    posts = app_db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# Post class(table) for app_db
class Post(app_db.Model):
    id = app_db.Column(app_db.Integer, primary_key=True)
    title = app_db.Column(app_db.String(100), nullable=False)
    date_posted = app_db.Column(app_db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = app_db.Column(app_db.Text, nullable=False)
    user_id = app_db.Column(app_db.Integer, app_db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/about')
@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/members')
@app.route('/members/')
def members():
    return render_template('members.html')


@app.route('/projects')
@app.route('/projects/')
def projects():
    return render_template('projects.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    return render_template('login.html', form=form)
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'valid_email_address' and form.password.data == 'checksum matches value stored':
            flash('Login Successful', 'success')
            return redirect(url_for('user_page'))
        else:
            flash('Login Unsuccessful')
            return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def registration_page():
    form = RegistrationForm()
    return render_templates('register.html', title='Register', form=form)

    if form.validate_on_submit():
        flash(f'Account creation successful for {form.username.data}', 'success')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
