from flask import Flask, session, render_template, redirect, url_for, request
from flask_session import Session  # Importiere Session von flask_session
from src.kumpelSuche import get_user

app = Flask(__name__, template_folder='src/html', static_folder='src/html')

# Flask-Session konfigurieren
app.config['SECRET_KEY'] = 'dein_geheimes_schlüssel'  # Setze einen geheimen Schlüssel
app.config['SESSION_TYPE'] = 'filesystem'  # Speicherung der Sitzung auf dem Dateisystem
Session(app)  # Initialisiere Flask-Session


@app.route('/')
def editProfile():

    return render_template('pages/editProfile.html')

@app.route('/profile')
def profile():
    if 'user_logged_in' not in session:
        return redirect(url_for('logging'))
    user_data = get_user(session['user_id'])
    return render_template('profile.html', username=user_data[0], email=user_data[1])


@app.route('/meinBereich', methods=['GET', 'POST'])
def meinBereich():
    if 'user_logged_in' not in session:
        return redirect(url_for('logging'))
    return render_template('pages/meinBereich.html')


@app.route('/', methods=['GET', 'POST'])
def kumpelSuche():
    if request.method == 'POST':
        username = request.form.get('username')
        user_data = get_user(username)
        if user_data:
            return render_template('pages/kumpelSuche.html', user_data=user_data)
        else:
            return render_template('pages/kumpelSuche.html', message="Kein Benutzer gefunden.")
    return render_template('pages/kumpelSuche.html')


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        return render_template('pages/meinBereich.html')

    return render_template('pages/create.html')


@app.route('/index')
def index():
    return render_template('pages/index.html')



@app.route('/kumpel_verwaltung')
def kumpel_verwaltung():
    if 'user_logged_in' not in session:
        return redirect(url_for('logging'))
    if request.method == 'POST':

        to_user = request.form.get('to_user_id')  # Korrekt aus dem Formular auslesen

        return render_template('pages/kumpels.html')

    return render_template('pages/kumpels.html')


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
