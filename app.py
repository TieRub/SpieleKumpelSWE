from flask import Flask, session, render_template, redirect, url_for, request
from flask_session import Session  # Importiere Session von flask_session

app = Flask(__name__, template_folder='src/html', static_folder='src/html')

# Flask-Session konfigurieren
app.config['SECRET_KEY'] = 'dein_geheimes_schlüssel'  # Setze einen geheimen Schlüssel
app.config['SESSION_TYPE'] = 'filesystem'  # Speicherung der Sitzung auf dem Dateisystem
Session(app)  # Initialisiere Flask-Session

@app.route('/')
def meinBereich():
    return render_template('pages/meinBereich.html')

@app.route('/create')
def create():
    return render_template('pages/create.html')

@app.route('/index')
def index():
    return render_template('pages/index.html')

@app.route('/profile')
def profile():
    if 'user_logged_in' not in session:
        return redirect(url_for('logging'))  # Wenn der Benutzer nicht eingeloggt ist, weiterleiten
    return render_template('pages/profile.html')

@app.route('/editProfile')
def editProfile():
    if 'user_logged_in' not in session:
        return redirect(url_for('logging'))
    return render_template('pages/editProfile.html')

@app.route('/kumpel_verwaltung')
def kumpel_verwaltung():
    if 'user_logged_in' not in session:
        return redirect(url_for('logging'))
    return render_template('pages/kumpels.html')

@app.route('/kumpelSuche')
def kumpelSuche():
    if 'user_logged_in' not in session:
        return redirect(url_for('logging'))
    return render_template('pages/kumpelSuche.html')

@app.route('/logging', methods=['GET', 'POST'])
def logging():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Beispielhafte Prüfung der Anmeldedaten
        if username == 'admin' and password == 'password':  # Beispielhafte Prüfung
            session['user_logged_in'] = True
            return redirect(url_for('profile'))  # Weiterleitung zur Profilseite

        # Wenn Login fehlschlägt
        return render_template('pages/logging.html', error='Invalid username or password')

    return render_template('pages/logging.html')

@app.route('/logout')
def logout():
    session.pop('user_logged_in', None)  # Benutzer aus der Sitzung entfernen
    return redirect(url_for('logging'))  # Zur Login-Seite weiterleiten

if __name__ == '__main__':
    app.run(debug=True)
