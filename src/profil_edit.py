from flask import Flask, render_template, request

app = Flask(__name__)
import sqlite3
from datetime import datetime

from flask import render_template, Flask, request, session, redirect, url_for

DATABASE = "C:/Users/victo/PycharmProjects/newOrderSWE/Spielekumpel-DB.sqlite"

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    return c


def get_user(username):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT username FROM users WHERE username = ?", (username,))
    result = c.fetchall()
    conn.close()
    return result


@app.route('/editProfil', methods=['POST'])
def edit():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    if request.method == 'POST':
        new_picture = request.form.get('new_picture')
        new_username = request.form.get('new_username')
        new_email = request.form.get('new_email')

        # Check if the new username is already taken
        c.execute("SELECT * FROM users WHERE username = ?", (new_username,))
        result = c.fetchall()

        if result:
            message = "Benutzername schon vergeben."
            return render_template('editProfileK.html', message=message)
        else:
            # Proceed with updating the user's profile
            c.execute("UPDATE users SET profile_picture = ?, username = ?, email = ? WHERE id = ?",
                      (new_picture, new_username, new_email, session['user_id']))
            conn.commit()
            return redirect(url_for('profile'))

    conn.close()