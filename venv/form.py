from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField
from wtforms.validators import DataRequired

class SubmitHash(FlaskForm):
    submit = SubmitField('Try it')
    
    



class HashGenerate(FlaskForm):
    string = StringField('')
    submit = SubmitField('Generate')


class HexGenerate(FlaskForm):
    string = StringField('',validators=[DataRequired()])
    submit = SubmitField('Generate')
    

    