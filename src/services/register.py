import sqlite3
from werkzeug.security import generate_password_hash

def register_user(username, password, email):
    """
    Register a new user in the database.

    Args:
        username (str): The desired username.
        password (str): The plaintext password.
        email (str): The user's email address.

    Returns:
        bool: True if registration is successful, False if the username already exists.
    """
    conn = sqlite3.connect('Spielekumpel-DB.sqlite')
    cursor = conn.cursor()

    # Check if the username already exists
    cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,))
    if cursor.fetchone()[0] > 0:
        conn.close()
        return False  # Username already exists

    # Hash the password
    hashed_password = generate_password_hash(password)

    # Insert the new user into the database
    cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                   (username, hashed_password, email))
    conn.commit()
    conn.close()
    return True
