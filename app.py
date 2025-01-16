from flask import Flask, render_template, redirect, url_for, request, flash, session
from src.services.login import login
from src.services.logout import logout
from src.services.register import register
from src.services.profile import profile_view

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
    def profile_view_route():
        return profile_view()

    # Logging Routes
    app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])
    app.add_url_rule('/register', view_func=register, methods=['GET', 'POST'])
    app.add_url_rule('/logout', view_func=logout)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8080)
