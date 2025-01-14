from flask import Flask, session, render_template, redirect, url_for, request
app = Flask(__name__, template_folder='src/html', static_folder='src')
@app.route('/index')
def index():
    return render_template('pages/index.html')

@app.route('/base')
def base():
    return render_template('pages/base.html')

@app.route('/logging')
def logging():
    return render_template('pages/logging.html')