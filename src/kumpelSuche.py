from src.database import get_user_profile, get_user, send_friend_request_db, get_user_id_by_username

from flask import render_template, Flask, request, session, redirect, url_for

def handle_friend_request():
    sender_username = session.get('username')
    receiver_username = request.form.get('receiver_username')

    if sender_username and receiver_username:
        # Hole die Benutzer-IDs anhand der Benutzernamen
        sender_id = get_user_id_by_username(sender_username)
        receiver_id = get_user_id_by_username(receiver_username)

        if sender_id and receiver_id:
            # Freundschaftsanfrage in der Datenbank speichern
            send_friend_request_db(sender_id, receiver_id)
            return redirect(url_for('kumpels'))
        else:
            return render_template('pages/kumpelSuche.html', error="Benutzer konnte nicht gefunden werden.")
    else:
        return redirect(url_for('login'))


