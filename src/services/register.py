from flask import request, flash, redirect, url_for, render_template
from src.services.database import register_user

def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        if register_user(username, password, email):
            return redirect(url_for('login'))
        else:
            flash('Username already exists, please choose a different one', 'error')
            return redirect(url_for('register'))
    return render_template('logging/register.html')
