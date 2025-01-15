import sqlite3
from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)

DATABASE = "C:/Users/spiel/PycharmProjects/SpieleKumpelSWE/Spielekumpel-DB.sqlite"

def get_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    return c

def get_event(id):
    c = get_db()
    suche = c.execute("SELECT LIST(creator_id, name, aktivitaet, max_mitglieder, description, datum, aktuelle_anzahl) FROM Events where id = ?", id)
    result = suche.fetchone()
    hostname = c.execute("SELECT LIST(username) from users where id = ?", result[0])
    owner = hostname.fetchone()[0]
    event_name = result[1]
    aktivitaet = result[2]
    max_mitglieder = result[3]
    description = result[4]
    datum = result[5]
    aktuelle_anzahl = result[6]
    return render_template('pages/meinBereich.html', event_name= event_name)





#create
@app.route('/createEvent', methods=['POST'])
def create_event():

    # Hole die Formulardaten
    name = request.form['name']
    aktivitaet = request.form['plan']
    oefentlich = 1 if 'oefentlich' in request.form else 0  # Überprüfen, ob die Checkbox aktiviert ist
    datum = request.form['datum']
    max_mitglieder = request.form['max_mitglieder']
    beschreibung = request.form['beschreibung']


    # Hole die Benutzer-ID und den Benutzernamen aus der Session
    creator_id = session['user_id']
    mitglieder = session['username']

    aktuelle_anzahl = 1

    # Datenbankeintrag für das Event erstellen
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO Events (creator_id, name, aktiviteat, max_mitglieder, oefentlich, datum, beschreibung, mitglieder, aktuelle_anzahl) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (creator_id, name, aktivitaet, max_mitglieder, oefentlich, datum, beschreibung, mitglieder, aktuelle_anzahl))
    conn.commit()
    conn.close()

    # Weiterleitung zur Seite "Mein Bereich" oder einer Bestätigungsseite
    return redirect(url_for('meinBereich'))  # Beispiel: Weiterleitung zur Seite "Mein Bereich"

