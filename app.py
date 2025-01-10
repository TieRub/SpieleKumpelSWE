from flask import Flask, render_template

app = Flask(__name__, template_folder='src/html/pages', static_folder='src/html')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/feed')
def feed():
    return render_template('feed.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/logging')
def logging():
    return render_template('logging.html')

if __name__ == '__main__':
    app.run(debug=True)

