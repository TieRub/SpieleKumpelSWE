import sqlite3
from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)

DATABASE = "C:/Users/spiel/PycharmProjects/SpieleKumpelSWE/Spielekumpel-DB.sqlite"

def get_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    return c

def get_event():
    c = get_db()
    c.execute("SELECT name FROM Events where oefentlich = true")
    result = c.fetchall()
    for row in result:
        if 'user_logged_in' not in session:
            print(row)
        else:
            c.execute("SELECT name FROM Events join users where users.id = ?", session['user_id'])
            result = c.fetchall()
            for row in result:
                print(row)

