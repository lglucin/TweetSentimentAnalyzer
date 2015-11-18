from flask import Flask, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Paiyge Sunnn!"

@app.route("/hello/<name>")
def hello(name):
	return "SUP FOO %s" % name

@app.route("/postHashTag", methods=['GET', 'POST'])
def postHashTag():
	if request.method =='POST':
		return "posted"
	else:
		return "got"



from wtforms import Form, BooleanField, TextField, PasswordField, validators

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])




if __name__ == "__main__":
    app.run()