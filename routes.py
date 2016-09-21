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

def createBody(form):
    text = """
    From: %s <%s>
    """ % (form.name.data, form.email.data)
    text += ""
    text += "APPLICATION"
    text += "Name: " + str(form.name.data) + "\n"
    text += "Email: " + str(form.email.data) + "\n"
    text += "Number of applicants: " + str(form.num_apps.data) + "\n"
    text += "Social Security Number: " + str(form.ssn.data) + "\n"
    text += "Move in Date: " + str(form.move_date.data) + "\n"
    text += "Lease Term: " + str(form.lease_term.data) + "\n"
    text += "DL Info: " + str(form.dl_info.data) + "\n"
    text += "Phone Number: " + str(form.phone.data) + "\n"
    text += "Pets: " + str(form.pets.data) + "\n"
    text += "Bankruptcies: " + str(form.bankruptcy.data) + "\n"
    text += "Felonies: " + str(form.felony.data) + "\n"
    text += "Evictions: " + str(form.eviction.data) + "\n"
    text += "Current Address: " + str(form.res1addr.data) + "\n"
    text += "From Date: " + str(form.res1from.data) + "\n"
    text += "To Date: " + str(form.res1to.data) + "\n"
    text += "Landlord Name: " + str(form.res1manager.data) + "\n"
    text += "Landlord Phone: " + str(form.res1phone.data) + "\n"
    text += "Previous Address: " + str(form.res2addr.data) + "\n"
    text += "From Date: " + str(form.res2from.data) + "\n"
    text += "To Date: " + str(form.res2to.data) + "\n"
    text += "Landlord Name: " + str(form.res2manager.data) + "\n"
    text += "Landlord Phone: " + str(form.res2phone.data) + "\n"
    text += "Current Employer: " + str(form.emp1addr.data) + "\n"
    text += "From Date: " + str(form.emp1from.data) + "\n"
    text += "To Date: " + str(form.emp1to.data) + "\n"
    text += "Supervisor Name: " + str(form.emp1manager.data) + "\n"
    text += "Supervisor Phone: " + str(form.emp1phone.data) + "\n"
    text += "Gross Income per Month: " + str(form.emp1income.data) + "\n"
    text += "Previous Employer: " + str(form.emp2addr.data) + "\n"
    text += "From Date: " + str(form.emp2from.data) + "\n"
    text += "To Date: " + str(form.emp2to.data) + "\n"
    text += "Supervisor Name: " + str(form.emp2manager.data) + "\n"
    text += "Supervisor Phone: " + str(form.emp2phone.data) + "\n"
    text += "Gross Income per Month: " + str(form.emp2income.data) + "\n"
    text += "Credit: " + str(form.credit.data) + "\n"
    text += "Accounts: " + str(form.accounts.data) + "\n"
    text += "Personal Reference 1: " + str(form.ref1addr.data) + "\n"
    text += "Length of aquaintance: " + str(form.ref1length.data) + "\n"
    text += "Personal Reference 1 Phone: " + str(form.ref1phone.data) + "\n"
    text += "Personal Reference 2: " + str(form.ref2addr.data) + "\n"
    text += "Length of aquaintance: " + str(form.ref2length.data) + "\n"
    text += "Personal Reference 2 Phone: " + str(form.ref2phone.data) + "\n"
    return text

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
        msg = Message("Application from " + form.name.data, sender='rentApp@tmagill.net', recipients=['mrthomasmagill@gmail.com'])
        msg.body = createBody(form)
        mail.send(msg)
        print msg.body

        return 'Your Application has been submitted.'

  elif request.method == 'GET':
    return render_template('apply.html', form=form)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=80)
