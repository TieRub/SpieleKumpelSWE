from flask import Flask, render_template, redirect, url_for, request, flash, session
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash

def create_app():
    app = Flask(__name__, template_folder='src/html/pages', static_folder='src/html')
    app.secret_key = 'your_secret_key'

    # Index Route
    @app.route('/')
    def index():
        return render_template('index.html')

    # Event Routes
    @app.route('/events_create')
    def events_create():
        return render_template('event/events_create.html')

    @app.route('/events_edit')
    def events_edit():
        return render_template('event/events_edit.html')

    @app.route('/events_view')
    def events_view():
        return render_template('event/events_view.html')

    # User Routes
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
        if 'user_logged_in' not in session:
            flash('Please log in to view your profile.', 'warning')
            return redirect(url_for('login'))

        user_id = session['user_id']
        conn = sqlite3.connect('Spielekumpel-DB.sqlite')
        cursor = conn.cursor()

        # Fetching user and profile details
        cursor.execute("""
            SELECT u.username, u.email, p.about_me 
            FROM users u
            LEFT JOIN profiles p ON u.id = p.user_id
            WHERE u.id = ?
        """, (user_id,))
        user_data = cursor.fetchone()
        conn.close()

        if user_data:
            username, email, about_me = user_data
        else:
            flash('User not found.', 'error')
            return redirect(url_for('index'))

        return render_template('user/profile_view.html', username=username, email=email, about_me=about_me)

    # Logging Routes
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user_id = validate_login(username, password)
            if user_id:
                session['user_logged_in'] = True
                session['user_id'] = user_id
                session['username'] = username
                flash(f'Welcome back, {username}!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Invalid username or password', 'error')
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
        session.clear()
        flash('You have been logged out.', 'info')
        return redirect(url_for('index'))

    return app

# Login validation function
def validate_login(username, password):
    conn = sqlite3.connect('Spielekumpel-DB.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT id, password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user[1], password):
        return user[0]
    return None

# Register function
def register_user(username, password, email):
    conn = sqlite3.connect('Spielekumpel-DB.sqlite')
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,))
    if cursor.fetchone()[0] > 0:
        conn.close()
        return False

    hashed_password = generate_password_hash(password)

    cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                   (username, hashed_password, email))
    conn.commit()

    user_id = cursor.lastrowid
    cursor.execute("INSERT INTO profiles (user_id, display_name) VALUES (?, ?)", (user_id, username))

    conn.commit()
    conn.close()
    return True

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8080)
