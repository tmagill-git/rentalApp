from flask import Flask, render_template, request, flash
from forms import ContactForm
 
app = Flask(__name__)      

app.secret_key = 'abcde12345'
 
@app.route('/')
def home():
  return render_template('index.html')

@app.route('/apply', methods=['GET', 'POST'])
def apply():
  form = ContactForm()
 
  if request.method == 'POST':
    print form.validate()
    if form.validate() == False:
        flash('All fields are required.')
        return render_template('apply.html', form=form)
    else:    
        return 'Form posted.'
 
  elif request.method == 'GET':
    return render_template('apply.html', form=form)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
