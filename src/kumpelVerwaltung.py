from django.shortcuts import render
from flask import Flask, request, jsonify, session, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user

from src import database

app = Flask(__name__)


@app.route('/kumpels')
def friends():
    friend = Friends.query.filter_by(status='friends').join()
    return render_template('kumpels.html')



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




