from flask import session, redirect, url_for, flash, render_template

def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))
