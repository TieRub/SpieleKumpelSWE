import sqlite3
from flask import Flask, request, jsonify, g

app = Flask(__name__)

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
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        db.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'message': 'Username already exists.'}), 400
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

    if user and user['password'] == password:  # Replace with bcrypt for production
        return jsonify({'message': 'Login successful!'}), 200
    return jsonify({'message': 'Invalid username or password.'}), 401

# Route: Logout
@app.route('/logout', methods=['POST'])
def logout():
    # Session management not implemented in this simplified version
    return jsonify({'message': 'Logged out successfully!'}), 200

# Route: Protected resource
@app.route('/protected', methods=['GET'])
def protected():
    # Authentication mechanism should be implemented for real use
    return jsonify({'message': 'Welcome to the protected resource!'}), 200

# Start the server
if __name__ == '__main__':
    app.run(debug=True)
