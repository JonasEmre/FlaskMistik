from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '863041e7e7d079ff31df64e4161229da'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    chars = db.relationship('Character', backref='owner', lazy=True)

    def __repr__(self):
        return f'Kullanıcı({self.username}, {self.email}, {self.image_file})'


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    strength = db.Column(db.Integer, nullable=False)
    dexterity = db.Column(db.Integer, nullable=False)
    intelligence = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @property
    def max_hp(self):
        return self.strength

    @property
    def max_mana(self):
        return self.intelligence

    @property
    def is_alive(self):
        if self.hp <= 0:
            return False
        else:
            return True

    def __repr__(self):
        return f'{self.name}'


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', chars=Character.query.all())


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'{form.username.data} için hesap oluşturuldu!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Kayıt Ol', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login kısmı yapım aşamasında.', 'danger')
        return redirect(url_for('home'))
    return render_template('login.html', title='Giriş', form=form)


if __name__ == '__main__':
    app.run(debug=True)
