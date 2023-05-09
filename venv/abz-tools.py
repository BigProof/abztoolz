from flask import Flask,flash,redirect,url_for,request,render_template
import colorama
from flask_wtf import FlaskForm
from form import SubmitHash
from form import HashGenerate
from form import HexGenerate
import hashlib



app = Flask(__name__)
app.config['SECRET_KEY'] = 'bigproof4ever'

@app.route('/')
def index():
    forms = SubmitHash()
    if forms.validate_on_submit():
        return redirect(url_for('hashh'))
    else:
        return render_template('index.html',forms=forms)


@app.route('/hash_Generator',methods=['POST','GET'])
def hashh():
    forms = HashGenerate()
    hash_gened=''
    if forms.validate_on_submit():
        inputt = forms.string.data
        if inputt:
            hashtext = hashlib.md5()
            hashtext.update(inputt.encode('utf-8'))
            hash_gened = hashtext.hexdigest()
            flash('MD5 Hash generated succusfully!')
            

        
    return render_template('hash.html', title='Hash Generator', forms=forms, hash=hash_gened)


@app.route('/Hex', methods=['POST','GET'])
def hexx():
    forms = HexGenerate()
    hex1 = ''
    if forms.validate_on_submit():
        inputt = forms.string.data
        if inputt:
            hex1 = inputt.encode('utf-8').hex()
            flash('Hex generated succusfully!')

    return render_template('hex.html', title='Hex Generator',forms=forms,hex=hex1)







if __name__ == '__main__':
    app.run(debug=True)
    