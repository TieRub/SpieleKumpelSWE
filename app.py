from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='src/html', static_folder='src/html')



@app.route('/')
def profile(post= 1):
    return render_template('pages/profile.html', username=post)

@app.route('/editProfile')
def editProfile():
    return render_template('pages/editProfile.html')

@app.route('/kumpel_verwaltung')
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

