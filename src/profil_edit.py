from flask import request, flash, redirect, url_for, render_template, session
from src.database import changeP


def editP():
    if request.method == 'POST':
        pic = request.form.get('picture')
        email = request.form.get('email')
        username = request.form.get('username')
        about = request.form.get('about')
        user_id = session.get('user_id')

        if not user_id:
            flash('User not logged in', 'error')
            return redirect(url_for('profile'))

        update = changeP(pic, username, email, user_id, about)

        if update:
            flash('Profile updated successfully!', 'success')
        else:
            flash('Failed to update profile.', 'error')

    return redirect(url_for('profile'))