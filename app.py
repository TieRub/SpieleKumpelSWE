from flask import Flask, render_template, redirect, url_for, request, flash
from src.services.login import validate_login
from src.services.register import register_user
from src.services.logout import logout

def create_app():
    app = Flask(__name__, template_folder='src/html/pages', static_folder='src/html')
    app.secret_key = 'your_secret_key'

# index.html
    @app.route('/')
    def index():
        return render_template('index.html')

#event
    @app.route('/events_create')
    def events_create():
        return render_template('event/events_create.html')
    @app.route('/events_edit')
    def events_edit():
        return render_template('event/events_edit.html')
    @app.route('/events_view')
    def events_view():
        return render_template('event/events_view.html')

#user
    @app.route('/friends_search')
    def friends_search():
        return render_template('user/friends_search.html')
    @app.route('/friends_view')
    def friends_view():
        return render_template('user/friends_view.html')
    @app.route('/profile_edit')
    def profile_edit():
        return render_template('user/profile_edit.html')
    @app.route('/profile_view')
    def profile_view():
        return render_template('user/profile_view.html')

#logging
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if validate_login(username, password):
                return redirect(url_for('index'))
            else:
                flash('Invalid username or password', 'error')
                return redirect(url_for('login'))
        return render_template('logging/login.html')
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            if register_user(username, password, email):
                return redirect(url_for('login'))
            else:
                flash('Username already exists, please choose a different one', 'error')
                return redirect(url_for('register'))
        return render_template('logging/register.html')
    @app.route('/logout')
    def logout_route():
        return logout()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8080)
