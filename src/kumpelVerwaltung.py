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


@app.route('/kumpels')
def friends(id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT username FROM Friends join users where id != ?", session['user_id'])
    result = c.fetchall()
    for row in result:
        print(row)

@app.route('/friendRequests_answer', methods=['POST'])
def friendRequests(request_id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    if request.method == 'POST':
        if request.form.get('answer') == 'accept':

            to_user_id = request.form.get('to_user_id')

            c.execute("INSERT INTO Friends (from_user_id, to_user_id) VALUES (?, ?)",
                      (to_user_id, session['user_id']))

            c.execute("DELETE FROM FriendRequest WHERE id = ?", request_id)
            conn.commit()
            return redirect(url_for('friends', id=request_id))
        else:
            c.execute("DELETE FROM FriendRequest WHERE from_user_id = ? AND to_user_id = ?",)



