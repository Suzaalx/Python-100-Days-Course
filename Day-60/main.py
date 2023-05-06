from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from flask_bootstrap import Bootstrap

class LoginForm(FlaskForm):
    username = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired(), Length(min=8, max=20)])
    submit = SubmitField('Sign In')
    

app = Flask(__name__)
Bootstrap(app)
app.secret_key= "mysecretkey"


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin@gmail.com' and form.password.data == 'admin123':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form) 


if __name__ == '__main__':
    app.run(debug=True)