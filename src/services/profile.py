from flask import render_template, redirect, url_for, flash, session
from src.services.database import get_user_profile

def profile_view():
    if 'user_logged_in' not in session:
        flash('Please log in to view your profile.', 'warning')
        return redirect(url_for('login'))

    user_id = session['user_id']
    user_data = get_user_profile(user_id)

    if user_data:
        username, email, about_me = user_data
    else:
        flash('User not found.', 'error')
        return redirect(url_for('index'))

    return render_template('user/profile_view.html', username=username, email=email, about_me=about_me)
