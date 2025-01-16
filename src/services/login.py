import sqlite3
from werkzeug.security import check_password_hash

def validate_login(username, password):
    """
    Validate the username and password provided during login.

    Args:
        username (str): The username provided by the user.
        password (str): The plaintext password provided by the user.

    Returns:
        int or None: The user ID if validation is successful, None otherwise.
    """
    conn = sqlite3.connect('Spielekumpel-DB.sqlite')
    cursor = conn.cursor()

    # Fetch the user ID and hashed password for the given username
    cursor.execute("SELECT id, password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user[1], password):
        return user[0]  # Return the user ID if the password matches
    return None
