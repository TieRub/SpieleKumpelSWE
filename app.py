from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin, login_user, LoginManager, login_required
from flask import render_template

app = Flask(__name__, template_folder='src/html', static_folder='src/html')


@app.route('/')
def kumpel_verwaltung():
    return render_template('pages/kumpels.html')


@app.route('/kumpelSuche')
def kumpelSuche():
    return render_template('pages/kumpelSuche.html')

@app.route('/logging')
def logging():
    return render_template('pages/logging.html')

if __name__ == '__main__':
    app.run(debug=True)

