import sqlite3
from datetime import datetime


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


def create_event(creator_id, name, max_mitglieder, oefentlich, datum):
    c = get_db()
    zwischen = c.execute("SELECT id FROM users where id = ?", (creator_id,))
    result = zwischen.fetchall()
    end = c.execute("SELECT username FROM users where id = ?", (creator_id,))
    erg = end.fetchone()
    anzahl = len(result)
    c.execute("INSERT INTO Events (creator_id, name, max_mitglieder, oefentlich, datum, mitglieder, aktuelle_anzahl) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (result[0][0], name, max_mitglieder, oefentlich, datum, erg[0], anzahl))
    c.execute('commit')

create_event(2,'Mega geilo Event', 4, 1, "2025-12-12")