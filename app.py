from flask import Flask, render_template

app = Flask(__name__, template_folder='src/html', static_folder='src/html')


@app.route('/')
def home():
    return render_template('pages/index.html')

@app.route('/feed')
def feed():
    return render_template('pages/feed.html')

@app.route('/profile')
def profile():
    return render_template('pages/profile.html')

@app.route('/logging')
def logging():
    return render_template('pages/logging.html')

@app.route('/navbar')
def navbar():
    return render_template('navbar/navbar.html')

@app.route('/base')
def base():
    return render_template('pages/base.html')

if __name__ == '__main__':
    app.run(debug=True)

