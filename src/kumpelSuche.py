from flask import Flask, request, jsonify, session, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_session import Session

# Flask-App initialisieren
app = Flask(__name__)

# Konfigurationen
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite-Datenbank
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Extensions initialisieren
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
Session(app)

# Datenbankmodell für Benutzer
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)


@app.route('/kumpelSuche', methods=['POST', 'GET'])
def suche():
    if request.method == 'POST':
        username = request.form.get('username')
        if not username:
            return render_template('pages/kumpelSuche.html', error="Kein Kumpel angegeben")

        user = User.query.filter_by(username=username).first()
        if user:
            return render_template('pages/kumpelSuche.html', user=user)
        else:
            return render_template('pages/kumpelSuche.html', message="Kumpel wurde nicht gefunden:(")
    return render_template('pages/kumpelSuche.html')



if __name__ == '__main__':
    app.run(debug=True)