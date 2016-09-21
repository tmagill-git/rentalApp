from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Message, Mail
from mail_creds import *

app.config["MAIL_SERVER"] = config["MAIL_SERVER"]
app.config["MAIL_PORT"] = config["MAIL_PORT"]
app.config["MAIL_USE_SSL"] = config["MAIL_USE_SSL"]
app.config["MAIL_USERNAME"] = config["MAIL_USERNAME"]
app.config["MAIL_PASSWORD"] = config["MAIL_PASSWORD"]

mail = Mail()

app = Flask(__name__)

app.secret_key = 'abcde12345'



mail.init_app(app)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/apply', methods=['GET', 'POST'])
def apply():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
        print form.validate()
        flash('All fields are required.')
        return render_template('apply.html', form=form)
    else:
        msg = Message("Test", sender='contact@example.com', recipients=['your_email@example.com'])
        msg.body = """
        From: %s <%s>
        %s
        """ % (form.name.data, form.email.data, form.pets.data)
        mail.send(msg)

        return 'Form posted.'

  elif request.method == 'GET':
    return render_template('apply.html', form=form)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
