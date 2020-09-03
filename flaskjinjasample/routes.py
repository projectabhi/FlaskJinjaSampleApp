from flask import render_template, url_for, flash, redirect
from flaskjinjasample.forms import RegistrationForm, LoginForm
from flaskjinjasample.models import User, Post
from flaskjinjasample import app

posts = [
    {
        'title': 'Blog Post 1',
        'content': 'Testing ginger with flask',
        'author': 'Abhijit Dey',
        'dateposted': '02-Sep-2020'
    },
    {
        'title': 'Blog Post 2',
        'content': 'Second Content',
        'author': 'Test User',
        'dateposted': '03-Sep-2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if (form.validate_on_submit()):
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))  # url_for accepts method name
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if (form.validate_on_submit()):
        if form.email.data == 'admin@admin.com' and form.password.data == 'password':
            flash(f'{form.email.data} logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful', 'danger')
    return render_template('login.html', title='Login', form=form)
