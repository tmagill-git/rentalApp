from flask_wtf import Form
from wtforms import StringField, SubmitField, validators, TextAreaField, ValidationError

class ContactForm(Form):
    name = StringField("Name",  [validators.InputRequired("Please enter your name.")])
    email = StringField("Email",  [validators.InputRequired("Please enter your email address.")])
    num_apps = StringField("Number of applicants",  [validators.InputRequired("Please enter the number of applicants.")])
    ssn = StringField("Social Security Number",  [validators.InputRequired("Please enter your SSN.")])
    move_date = StringField("Move in Date",  [validators.InputRequired("Please enter the move-in date.")])
    lease_term = StringField("Lease Term (1 or 2 Years)",  [validators.InputRequired("Please enter the lease term.")])
    dl_info = StringField("Driver's license State and Number",  [validators.InputRequired("Please enter Driver's License info.")])
    phone = StringField("Phone Number",  [validators.InputRequired("Please enter a phone number.")])
    pets = TextAreaField("Will there be any pets?  If so, describe type and weight.")
    bankruptcy = TextAreaField("Has applicant been a party to an unlawful detainer action or filed bankruptcy within the last seven years?  If so, please explain.",  [validators.InputRequired("Please answer no, or explain")])
    felony = TextAreaField("Has applicant or any proposed occupant ever been convicted of or pleaded no contest to a felony?  If so, please explain.",  [validators.InputRequired("Please answer no, or explain")])
    eviction = TextAreaField("Has applicant or any proposed occupant ever been evicted from a residence?  If so, please explain.",  [validators.InputRequired("Please answer no, or explain")])

    res1addr = StringField("Current Address",  [validators.InputRequired("Please enter current address.")])
    res1from = StringField("From Date",  [validators.InputRequired("Please complete current address information.")])
    res1to = StringField("To Date",  [validators.InputRequired("Please complete current address information.")])
    res1manager = StringField("Landlord Name",  [validators.InputRequired("Please complete current address information.")])
    res1phone = StringField("Landlord Phone",  [validators.InputRequired("Please complete current address information.")])

    res2addr = StringField("Previous Address",  [validators.InputRequired("Please enter previous address.")])
    res2from = StringField("From Date",  [validators.InputRequired("Please complete previous address information.")])
    res2to = StringField("To Date",  [validators.InputRequired("Please complete previous address information.")])
    res2manager = StringField("Landlord Name",  [validators.InputRequired("Please complete previous address information.")])
    res2phone = StringField("Landlord Phone",  [validators.InputRequired("Please complete previous address information.")])

    emp1addr = StringField("Current Employer",  [validators.InputRequired("Please enter current employer.")])
    emp1from = StringField("From Date",  [validators.InputRequired("Please complete current employer information.")])
    emp1to = StringField("To Date",  [validators.InputRequired("Please complete current employer information.")])
    emp1manager = StringField("Supervisor Name",  [validators.InputRequired("Please complete current employer information.")])
    emp1phone = StringField("Supervisor Phone",  [validators.InputRequired("Please complete current employer information.")])
    emp1income = StringField("Gross Income per Month",  [validators.InputRequired("Please complete current employer information.")])
    emp2addr = StringField("Previous Employer",  [validators.InputRequired("Please enter previous employer.")])
    emp2from = StringField("From Date",  [validators.InputRequired("Please complete previous employer information.")])
    emp2to = StringField("To Date",  [validators.InputRequired("Please complete previous employer information.")])
    emp2manager = StringField("Supervisor Name",  [validators.InputRequired("Please complete previous employer information.")])
    emp2phone = StringField("Supervisor Phone",  [validators.InputRequired("Please complete previous employer information.")])
    emp2income = StringField("Gross Income per Month",  [validators.InputRequired("Please complete previous employer information.")])
    credit = TextAreaField("Please list creditors, monthly payments, and account balances.  If you know your credit score, you can enter it here as well.",  [validators.InputRequired("Please enter credit info.")])
    accounts = TextAreaField("Please list account types (checking/savings/etc) balances.")
    ref1addr = StringField("Personal Reference 1",  [validators.InputRequired("Please enter personal reference.")])
    ref1length = StringField("Length of aquaintance",  [validators.InputRequired("Please complete personal reference information.")])
    ref1phone = StringField("Personal Reference 1 Phone",  [validators.InputRequired("Please complete personal reference information.")])
    ref2addr = StringField("Personal Reference 2",  [validators.InputRequired("Please enter personal reference.")])
    ref2length = StringField("Length of aquaintance",  [validators.InputRequired("Please complete personal reference information.")])
    ref2phone = StringField("Personal Reference 2 Phone",  [validators.InputRequired("Please complete personal reference information.")])
    submit = SubmitField("Send")
