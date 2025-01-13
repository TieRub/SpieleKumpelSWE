from django.shortcuts import render
from flask import Flask, request, jsonify, session, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user

from src import database

app = Flask(__name__)


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




