from flask import Flask, render_template, redirect, url_for, request, session
from flask_session import Session
from src.database import get_user_profile, get_user, send_friend_request_db
from src.login import login
from src.logout import logout
from src.register import register
from src.kumpelSuche import handle_friend_request
from src.profil_edit import editP

app = Flask(__name__, template_folder='src/html', static_folder='src/html')

# Flask-Session konfigurieren
app.config['SECRET_KEY'] = 'dein_geheimes_schlüssel'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.route('/send_friend_request/<receiver_id>', methods=['POST'])
def send_friend_request_route(receiver_id):
    sender_id = request.form.get('sender_id')  # sender_id aus dem Formular
    kumpel_verwaltung(sender_id, receiver_id)  # Funktionsaufruf
    return redirect(url_for('kumpels', receiver_id=receiver_id))


@app.route('/editProfile', methods=['POST', 'GET'])
def editProfile():
    if 'user_logged_in' not in session:
        return redirect(url_for('login'))

    user = session['user_id']
    user_data = get_user_profile(user)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        picture = request.form['profile_picture']


        editP(user, name, email, picture)

        return redirect(url_for('profile'))


    return render_template(
        'pages/editProfile.html',
        name=user_data[0],
        email=user_data[1],
        picture=user_data[2],
        user_id=user
    )




@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_logged_in' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    user_data = get_user_profile(user_id)
    return render_template('pages/profile.html', username=user_data[0], email=user_data[1])






@app.route('/kumpels', methods=['GET', 'POST'])
def kumpels():
    receiver_id = request.args.get('receiver_id')  # receiver_id aus der URL holen
    return render_template('pages/kumpels.html', receiver_id=receiver_id)




@app.route('/meinBereich', methods=['GET', 'POST'])
def meinBereich():
    return render_template('pages/meinBereich.html')




@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        return render_template('pages/meinBereich.html')
    return render_template('pages/create.html')





@app.route('/')
def index():
    return render_template('pages/index.html')





@app.route('/kumpel_verwaltung', methods=['GET', 'POST'])
def kumpel_verwaltung():
    # Weitere Logik für Freundschaftsanfragen hinzufügen
    return render_template('pages/kumpels.html')





@app.route('/kumpel_suche', methods=['GET', 'POST'])
def kumpelSuche():
    if request.method == 'POST':
        username = request.form.get('username')
        user_data = get_user(username)
        if user_data:
            return render_template('pages/kumpelSuche.html', user_data=user_data)
        else:
            return render_template('pages/kumpelSuche.html', message="Kein Benutzer gefunden.")
    return render_template('pages/kumpelSuche.html')



# Logging Routes
app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])
app.add_url_rule('/register', view_func=register, methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=logout)

if __name__ == '__main__':
    app.run(debug=True)
