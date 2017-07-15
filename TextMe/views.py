from TextMe import app
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
import os
from .models import User, db
from .forms import *
from flask_login import LoginManager

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)



@app.route('/index')
def index():
    return '<h1>Hello world</h1>'

@login_manager.user_loader
def user_loader(user_id):
    """Given user_id, return the associated User object."""
    return User.query.get(user_id)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        if not User.query.filter_by(username=form.username.data).first():
            new_user = User(form.username.data, form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash('User successfully registered')
            return redirect(url_for('goals'))
        else:
            flash('User already exists')
    return render_template('register.html', form=form)

#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    """For GET requests, display login form, for POSTS, login the user by processing data."""
#    form = LoginForm(request.form)
#    if request.method == 'POST' and form.validate():
#        user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
#        return redirect(url_for('goals'))
#    return render_template('login.html', form=form)

@app.route('/goals')
def goals():
    return '<h1>Goals<h1>'
