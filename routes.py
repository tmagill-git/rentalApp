from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Message, Mail
import mail_creds



mail = Mail()

app = Flask(__name__)

app.secret_key = 'abcde12345'

app.config["MAIL_SERVER"] = mail_creds.MAIL_SERVER
app.config["MAIL_PORT"] = mail_creds.MAIL_PORT
app.config["MAIL_USE_SSL"] = mail_creds.MAIL_USE_SSL
app.config["MAIL_USERNAME"] = mail_creds.MAIL_USERNAME
app.config["MAIL_PASSWORD"] = mail_creds.MAIL_PASSWORD

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
        return render_template('apply.html', form=form)
    else:
        msg = Message("Test", sender='rentApp@tmagill.net', recipients=['estrella@tmagill.net'])
        msg.body = """
        From: %s <%s>
        %s
        """ % (form.name.data, form.email.data, form.pets.data)
        mail.send(msg)
        print msg.body

        return 'Your Application has been submitted.'

  elif request.method == 'GET':
    return render_template('apply.html', form=form)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
