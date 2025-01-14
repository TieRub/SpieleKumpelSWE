from flask import Flask, render_template, redirect, url_for, request, flash
from src.services.login import validate_login
from src.services.register import register_user
from src.services.logout import logout

def create_app():
    # Correct the template and static folder paths
    app = Flask(__name__, template_folder='src/html/pages', static_folder='src/html/assets')
    app.secret_key = 'your_secret_key'  # Required for flashing messages in Flask

    # Home route (index.html)
    @app.route('/')
    def index():
        return render_template('index.html')  # Ensure the correct path based on 'src/html/pages'

    # Login route (login.html)
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if validate_login(username, password):
                return redirect(url_for('index'))  # Redirect to home after successful login
            else:
                flash('Invalid username or password', 'error')
                return redirect(url_for('login'))
        return render_template('logging/login.html')  # Corrected the typo here

    # Register route (register.html)
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            if register_user(username, password, email):
                return redirect(url_for('login'))  # Redirect to login page after successful registration
            else:
                flash('Username already exists, please choose a different one', 'error')
                return redirect(url_for('register'))
        return render_template('logging/register.html')

    # Logout route
    @app.route('/logout')
    def logout_route():
        return logout()  # Ensure your logout function handles the session properly

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8080)  # Set the port to 8080
