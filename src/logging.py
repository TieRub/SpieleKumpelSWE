import sqlite3
from flask import Flask, request, jsonify, g

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Sicherheitsschlüssel für Sessions

DATABASE = 'users.db'

# Helper function to get a database connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row  # Return rows as dictionaries
    return db

# Cleanup database connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Route: Register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    if not email or not username or not password:
        return jsonify({'message': 'Email, Username and password are required.'}), 400

    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (email, username, password) VALUES (?, ?, ?)", (email, username, password))
        db.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'message': 'Username or email already exists.'}), 400
    except Exception as e:
        return jsonify({'message': 'An error occurred.', 'error': str(e)}), 500

# Route: User login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    if user and user['password'] == password:  # Hier könntest du bcrypt zur Passwortsicherung verwenden
        # Erfolgreiches Login: Session setzen
        session['user_id'] = user['id']
        return jsonify({'message': 'Login successful!'}), 200
    return jsonify({'message': 'Invalid username or password.'}), 401

# Route: Logout
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # Benutzer aus der Sitzung entfernen
    return jsonify({'message': 'Logged out successfully!'}), 200

# Route: Protected resource
@app.route('/profile', methods=['GET'])
def profile():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401  # Nur authentifizierte Benutzer können auf das Profil zugreifen

    user_id = session['user_id']
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()

    if user:
        return jsonify({
            'username': user['username'],
            'email': user['email'],
            'profile_picture': user['profile_picture']
        })
    return jsonify({'message': 'User not found'}), 404

# Start the server
if __name__ == '__main__':
    app.run(debug=True)
