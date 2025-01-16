import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash

def get_db_connection():
    conn = sqlite3.connect('Spielekumpel-DB.sqlite')
    return conn

def validate_login(username, password):
    """
    Validate the username and password provided during login.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user[1], password):
        return user[0]
    return None

def register_user(username, password, email):
    """
    Register a new user in the database and automatically create a profile.
    """
    conn = get_db_connection()
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
    cursor.execute("INSERT INTO profiles (user_id, display_name) VALUES (?, ?)", (user_id, username))
    conn.commit()
    conn.close()
    return True

def get_user_profile(user_id):
    """
    Fetch the user's profile details.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT u.username, u.email, p.about_me 
        FROM users u
        LEFT JOIN profiles p ON u.id = p.user_id
        WHERE u.id = ?
    """, (user_id,))
    user_data = cursor.fetchone()
    conn.close()

    return user_data
