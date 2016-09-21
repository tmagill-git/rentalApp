from flask_wtf import Form
from wtforms import TextField, SubmitField, validators, TextAreaField, ValidationError

class ContactForm(Form):
    name = TextField("Name",  [validators.Required("Please enter your name.")])
    email = TextField("Email",  [validators.Required("Please enter your email address.")])
    #
    # num_apps = TextField("Number of applicants",  [validators.Required("Please enter the number of applicants.")])
    # ssn = TextField("Social Security Number",  [validators.Required("Please enter your SSN.")])
    # move_date = TextField("Move in Date",  [validators.Required("Please enter the move-in date.")])
    # lease_term = TextField("Lease Term (1 or 2 Years)",  [validators.Required("Please enter the lease term.")])
    # dl_info = TextField("Driver's license State and Number",  [validators.Required("Please enter Driver's License info.")])
    # phone = TextField("Phone Number",  [validators.Required("Please enter a phone number.")])
    pets = TextAreaField("Will there be any pets?  If so, describe type and weight.")
    # bankruptcy = TextAreaField("Has applicant been a party to an unlawful detainer action or filed bankruptcy within the last seven years?  If so, please explain.")
    # felony = TextAreaField("Has applicant or any proposed occupant ever been convicted of or pleaded no contest to a felony?  If so, please explain.")
    # eviction = TextAreaField("Has applicant or any proposed occupant ever been evicted from a residence?  If so, please explain.")
    #
    # res1addr = TextField("Current Address",  [validators.Required("Please enter current address.")])
    # res1from = TextField("From Date",  [validators.Required("Please complete current address information.")])
    # res1to = TextField("To Date",  [validators.Required("Please complete current address information.")])
    # res1manager = TextField("Landlord Name",  [validators.Required("Please complete current address information.")])
    # res1phone = TextField("Landlord Phone",  [validators.Required("Please complete current address information.")])
    #
    # res2addr = TextField("Previous Address",  [validators.Required("Please enter previous address.")])
    # res2from = TextField("From Date",  [validators.Required("Please complete previous address information.")])
    # res2to = TextField("To Date",  [validators.Required("Please complete previous address information.")])
    # res2manager = TextField("Landlord Name",  [validators.Required("Please complete previous address information.")])
    # res2phone = TextField("Landlord Phone",  [validators.Required("Please complete previous address information.")])
    #
    # emp1addr = TextField("Current Employer",  [validators.Required("Please enter current employer.")])
    # emp1from = TextField("From Date",  [validators.Required("Please complete current employer information.")])
    # emp1to = TextField("To Date",  [validators.Required("Please complete current employer information.")])
    # emp1manager = TextField("Supervisor Name",  [validators.Required("Please complete current employer information.")])
    # emp1phone = TextField("Supervisor Phone",  [validators.Required("Please complete current employer information.")])
    # emp1income = TextField("Gross Income per Month",  [validators.Required("Please complete current employer information.")])
    #
    # emp2addr = TextField("Previous Employer",  [validators.Required("Please enter previous employer.")])
    # emp2from = TextField("From Date",  [validators.Required("Please complete previous employer information.")])
    # emp2to = TextField("To Date",  [validators.Required("Please complete previous employer information.")])
    # emp2manager = TextField("Supervisor Name",  [validators.Required("Please complete previous employer information.")])
    # emp2phone = TextField("Supervisor Phone",  [validators.Required("Please complete previous employer information.")])
    # emp2income = TextField("Gross Income per Month",  [validators.Required("Please complete previous employer information.")])
    #
    # credit = TextAreaField("Please list creditors, monthly payments, and account balances.  If you know your credit score, you can enter it here as well.",  [validators.Required("Please enter credit info.")])
    # accounts = TextAreaField("Please list account types (checking/savings/etc) balances.")
    #
    # ref1addr = TextField("Personal Reference 1",  [validators.Required("Please enter personal reference.")])
    # ref1length = TextField("Length of aquaintance",  [validators.Required("Please complete personal reference information.")])
    # ref1phone = TextField("Personal Reference 1 Phone",  [validators.Required("Please complete personal reference information.")])
    #
    # ref2addr = TextField("Personal Reference 2",  [validators.Required("Please enter personal reference.")])
    # ref2length = TextField("Length of aquaintance",  [validators.Required("Please complete personal reference information.")])
    # ref2phone = TextField("Personal Reference 2 Phone",  [validators.Required("Please complete personal reference information.")])
	
    submit = SubmitField("Send")
