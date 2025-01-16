import sqlite3
from werkzeug.security import generate_password_hash

def register_user(username, password, email):
    """
    Register a new user in the database and automatically create a profile.

    Args:
        username (str): The desired username.
        password (str): The plaintext password.
        email (str): The user's email address.

    Returns:
        bool: True if registration is successful, False if the username already exists.
    """
    conn = sqlite3.connect('Spielekumpel-DB.sqlite')
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,))
    if cursor.fetchone()[0] > 0:
        conn.close()
        return False

    hashed_password = generate_password_hash(password)

    cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                   (username, hashed_password, email))
    conn.commit()

    user_id = cursor.lastrowid

    cursor.execute("INSERT INTO profiles (user_id, display_name) VALUES (?, ?)",
                   (user_id, username))

    conn.commit()
    conn.close()
    return True
