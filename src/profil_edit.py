from flask import Flask, render_template, request
from sqlalchemy.orm import sessionmaker
from src.database import db_session  # Assuming db_session is correctly defined in your src.database module

from src.models import User  # Assuming User model is defined here

app = Flask(__name__)


@app.route('/editProfil', methods=['POST'])
def edit():
    # Check if the button is pressed (handled via form submission)
    if request.method == 'POST':
        new_picture = request.form.get('new_picture')
        new_username = request.form.get('new_username')
        new_email = request.form.get('new_email')
        new_Vornamen = request.form.get('new_Vornamen')
        new_Nachname = request.form.get('new_Nachname')

        # Check if the username already exists
        if db_session.query(User).filter_by(username=new_username).first():
            return "Username already exists"

        # Updating user information
        user = db
