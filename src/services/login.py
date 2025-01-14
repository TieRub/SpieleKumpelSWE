import sqlite3
from werkzeug.security import check_password_hash


def validate_login(username, password):
    conn = sqlite3.connect('Spielekumpel-DB.sqlite')
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    stored_password = cursor.fetchone()

    conn.close()

    if stored_password:
        return check_password_hash(stored_password[0], password)
    return False
