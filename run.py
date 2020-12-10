from flask import Flask, render_template, url_for
from characters import Character, temp_chars

app = Flask(__name__)

habel = Character('Habel', 90, 90, 45)
cain = Character('Cain', 90, 100, 35)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', chars=temp_chars)


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
