from flask import request, flash, redirect, url_for, session, render_template
from src.services.database import validate_login

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_id = validate_login(username, password)
        if user_id:
            session['user_logged_in'] = True
            session['user_id'] = user_id
            session['username'] = username
            flash(f'Welcome back, {username}!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('logging/login.html')
