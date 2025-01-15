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


# Suchen

@app.route('/kumpelSuche', methods=['GET', 'POST'])
def kumpelSuche():
    if request.method == 'POST':
        username = request.form.get('username')

        # Debugging-Ausgabe
        print(f"Suche nach Benutzer: {username}")

        try:
            user_data = get_user(username)
            if user_data:
                return render_template('pages/kumpelSuche.html', user_data=user_data)
            else:
                return render_template('pages/kumpelSuche.html', message="Kein Benutzer gefunden.")
        except Exception as e:
            print(f"Fehler: {e}")
            return render_template('pages/kumpelSuche.html', error="Ein Fehler ist aufgetreten.")
    return render_template('pages/kumpelSuche.html')


# Anfragen

@app.route('/freundschaftsAnfrage', methods=['POST'])
def freundschaftsAnfrage():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    to_user = request.form.get('to_user_id')  # Korrekt aus dem Formular auslesen
    try:
        c.execute("INSERT INTO FriendRequest (from_user_id, to_user_id) VALUES (?, ?)",
                  (session['user_id'], to_user))
        conn.commit()
        message = "Freundschaftsanfrage erfolgreich gesendet!"
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        message = "Ein Fehler ist aufgetreten!"
    finally:
        conn.close()

    return render_template('pages/kumpels.html', new_friend_request=message)
