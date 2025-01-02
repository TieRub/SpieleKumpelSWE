from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class UserDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(15), nullable=False)
    description = db.Column(db.String(255), nullable=True)


class EventDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    amount_of_people = db.Column(db.Integer, nullable=False)
    private = db.Column(db.Boolean, nullable=False)
    description = db.Column(db.String(300), nullable=True)
    date = db.Column(db.DateTime, nullable=True)
    owner_username = db.Column(db.String(20), db.ForeignKey('user.username'), nullable=False)
    participants = db.Column(db.String(200), nullable=True)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
