from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import data_required, length, equal_to, email


class RegistrationForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[data_required(), length(min=5, max=12)])
    email = StringField('E-mail', validators=[data_required()])
    password = PasswordField('Şifre', validators=[data_required()])
    confirm_password = PasswordField('Şifre Tekrar', validators=[data_required(), equal_to('password')])
    submit = SubmitField('Kayıt Ol')


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[data_required()])
    password = PasswordField('Şifre', validators=[data_required()])
    remember = BooleanField('Beni Hatırla')
    submit = SubmitField('Giriş')
