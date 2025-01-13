from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_session import Session

# Flask-App initialisieren
app = Flask(__name__)

# Konfigurationen
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite-Datenbank
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkey'  # Wähle einen sicheren Schlüssel
app.config['SESSION_TYPE'] = 'filesystem'

# Extensions initialisieren
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
Session(app)

# Datenbankmodell für Benutzer
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Datenbank erstellen (nur einmal ausführen)
@app.before_request
def create_tables():
    with app.app_context():
        db.create_all()

# Route: Benutzerkonto erstellen
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username und Passwort sind erforderlich.'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Benutzername existiert bereits.'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Benutzer erfolgreich registriert!'}), 201

# Route: Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username und Passwort sind erforderlich.'}), 400

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        session['user_id'] = user.id
        return jsonify({'message': 'Login erfolgreich!'}), 200
    else:
        return jsonify({'message': 'Ungültiger Benutzername oder Passwort.'}), 401

# Route: Logout
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Erfolgreich ausgeloggt!'}), 200

# Route: Geschützte Ressource (nur für eingeloggte Benutzer)
@app.route('/protected', methods=['GET'])
def protected():
    if 'user_id' not in session:
        return jsonify({'message': 'Nicht autorisiert.'}), 401
    return jsonify({'message': 'Willkommen zur geschützten Ressource!'}), 200

# Server starten
if __name__ == '__main__':
    app.run(debug=True)
