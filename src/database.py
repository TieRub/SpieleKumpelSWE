import sqlite3
from flask import session
from django.dispatch import receiver
from werkzeug.security import check_password_hash, generate_password_hash


def get_db_connection():
    conn = sqlite3.connect('Spielekumpel-DB.sqlite')
    print("Connection successful!")

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
    Fetch the user's profile details including the profile picture.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT u.username, u.email, p.about_me, p.profile_picture
        FROM users u
        LEFT JOIN profiles p ON u.id = p.user_id
        WHERE u.id = ?
    """, (user_id,))
    user_data = cursor.fetchone()
    conn.close()

    return user_data
def get_user_id_by_username(username):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return user[0]  # Gibt die Benutzer-ID zurück
    return None

def get_user(name):
    """
    Suche nach Benutzern basierend auf dem Benutzernamen (teilweise Übereinstimmung möglich).
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # Verwende LIKE für Teilstring-Suche
    cursor.execute("""
        SELECT u.username, p.profile_picture
        FROM users u
        LEFT JOIN profiles p ON u.id = p.user_id
        WHERE u.username = ? ;
    """, (name,))
    users = cursor.fetchall()
    conn.close()

    return users

def send_friend_request_db(sender_id, receiver_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO friend_pending (sender_id, receiver_id)
        VALUES (?, ?)
    """, (sender_id, receiver_id))
    conn.commit()
    conn.close()


def changeP(new_picture, new_username, new_email, user_id, about):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE profiles p
            JOIN users u ON p.user_id = u.id
            SET p.profile_picture = ?, 
                p.display_name = ?, 
                u.email = ?, 
                u.username = ?, 
                p.about_me = ?
            WHERE u.id = ?
        """, (new_picture, new_username, new_email, new_username, about, user_id))
        conn.commit()
        return cursor.rowcount > 0  # Return True if rows updated
    except Exception as e:
        print(f"Database Error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def getEvent():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT u.username, p.profile_picture
        FROM users u
        LEFT JOIN profiles p ON u.id = p.user_id
        WHERE u.username = ? ;
    """, (name,))
    users = cursor.fetchall()
    conn.close()

    return users

def index():
    conn = get_db_connection()
    cursor = conn.cursor()





