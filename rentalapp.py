from flask import Flask, render_template, request, send_file
from forms import ContactForm
from flask_mail import Message, Mail
import mail_creds
import math


mail = Mail()

app = Flask(__name__)

app.secret_key = 'abcde12345'

app.config["MAIL_SERVER"] = mail_creds.MAIL_SERVER
app.config["MAIL_PORT"] = mail_creds.MAIL_PORT
app.config["MAIL_USE_SSL"] = mail_creds.MAIL_USE_SSL
app.config["MAIL_USERNAME"] = mail_creds.MAIL_USERNAME
app.config["MAIL_PASSWORD"] = mail_creds.MAIL_PASSWORD

mail.init_app(app)

class rentObject():
    def __init__(self, price, hoa, rent, dp, rate):
        if float(price) <= 1000:
            self.price = float(price) * 1000
        else:
            self.price = float(price)
        self.hoa = float(hoa)
        self.rent = float(rent)
        self.dp = self.price * int(dp) / 100
        self.rate = float(rate) / (100 * 12)
        self.finance = self.price - self.dp
        self.monthly = self.finance * (self.rate / (1 - math.pow((1 + self.rate), (- 360))))
        # self.principal = round(self.finance / 741, 2)
        self.principal = round(self.monthly * .249, 2)
        self.tax = self.price * .01179 / 12
        self.insurance = 30
        self.cash = self.rent - self.monthly - self.hoa - self.tax - self.insurance
        self.income = self.principal + self.cash
        self.roc = "{0:.0f}%".format(self.income * 1200 / self.dp)
        self.appreciation = self.price * .02 / 12
        self.xroc = "{0:.0f}%".format(((self.income + self.appreciation) * 1200 / self.dp) -4)

def createBody(form):
    text = """
    From: %s <%s>
    """ % (form.name.data, form.email.data)
    text += ""
    text += "APPLICATION"
    text += "Name: " + str(form.name.data) + "\n"
    text += "Email: " + str(form.email.data) + "\n"
    text += "Number of applicants: " + str(form.num_apps.data) + "\n"
    text += "Other Occupants: " + str(form.other_occ.data) + "\n"
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

        return render_template('screening.html')

  elif request.method == 'GET':
    return render_template('apply.html', form=form)


@app.route('/analysis')
def analysis():
    html = render_template('analysis.html')
    return html
    return

@app.route('/analysis_post', methods=['POST'])
def analysis_post():
    price = request.form['price']
    hoa = request.form['hoa']
    rent = request.form['rent']
    dp = request.form['dp']
    rate = request.form['rate']
    house = rentObject(price, hoa, rent, dp, rate)
    print house.roc, house.xroc, house.appreciation
    html = render_template('analysis_post.html', house=house)
    return html



if __name__ == '__main__':
  app.run()