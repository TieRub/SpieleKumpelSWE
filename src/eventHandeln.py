import sqlite3
from datetime import datetime
from urllib import request

from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)

DATABASE = "C:/Users/spiel/PycharmProjects/SpieleKumpelSWE/Spielekumpel-DB.sqlite"

def get_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    return c

def get_event(id):
    c = get_db()
    c.execute("SELECT name FROM Events where id = ?", id)
    result = c.fetchall()
    for row in result:
        print(row)




#create
@app.route('/createEvent', methods=['POST'])
def create_event(creator_id, name, max_mitglieder, oefentlich, datum):
    conn = get_db()
    c = conn.cursor()

    creator_id = session['user_id']
    name = request.form.get('name')
    max_mitglieder = request.form.get('max_mitglieder')
    oefentlich = request.form.get('oefentlich')
    datum = request.form.get('datum')

    c.execute(""
              "INSERT INTO Events (creator_id, name, max_mitglieder, oefentlich, description, datum, aktuelle_anzahl) "
              "VALUES (?, ?, ?, ?, ?, ?, ?)",
              (creator_id, name, max_mitglieder, oefentlich, datum, 1 ))
    conn.commit()
    message = f"Event '{name}' wurde erfolgreich erstellt!"
    return render_template('pages/meinBereich.html', message=message)


@app.route('/createEvent', methods=['POST'])
def create_event():

    # Hole die Formulardaten
    name = request.form['name']
    plan = request.form['plan']
    oefentlich = 1 if 'oefentlich' in request.form else 0  # Überprüfen, ob die Checkbox aktiviert ist
    datum = request.form['datum']
    beschreibung = request.form['beschreibung']

    # Hole die Benutzer-ID aus der Session
    creator_id = session['user_id']

    # Datenbankeintrag für das Event erstellen
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO Events (creator_id, name, plan, oefentlich, datum, beschreibung) VALUES (?, ?, ?, ?, ?, ?)",
              (creator_id, name, plan, oefentlich, datum, beschreibung))
    conn.commit()
    conn.close()

    # Weiterleitung zur Seite "Mein Bereich" oder einer Bestätigungsseite
    return redirect(url_for('meinBereich'))  # Beispiel: Weiterleitung zur Seite "Mein Bereich"

