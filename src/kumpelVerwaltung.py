from django.shortcuts import render
from flask import Flask, request, jsonify, session, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user

from src.kumpelSuche import User

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    friends_from = db.relationship('Friends', foreign_keys=[Friends.friend_from_id])
    friends_to = db.relationship('Friends', foreign_keys=[Friends.friend_to_id])
    friend_requests_sent = db.relationship('FriendRequest', foreign_keys=[FriendRequest.friend_from_id])
    friend_requests_received = db.relationship('FriendRequest', foreign_keys=[FriendRequest.friend_to_id])



class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    friend_from_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    friend_to_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class FriendRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    friend_from_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    friend_to_id = db.Column(db.Integer, db.ForeignKey('user.id'))


@app.route('/kumpels')
@login_required
def friends():
    user = User.query.get(current_user.id)
    friends = user.friends_from + user.friends_to
    requests = user.friend_requests_received
    no_friends = [req.friend_from for req in user.friend_requests_sent if req.status == 'pending']

    return render_template('kumpels.html', friends=friends, requests=requests, no_friends=no_friends)



def friendRequests(request_id):
    action = request.form.get('action')
    friend_request = FriendRequest.query.filter_by(request_id)

    if action == 'accept':
        friend = Friends(friend_from_id=friend_request.friend_from_id, friend_to_id=friend_request.friend_to_id)
        db.session.add(friend)
        db.session.delete(friend_request)

    elif action == 'decline':
        db.session.delete(friend_request)

    db.session.commit()
    return redirect(url_for('kumpels'))




