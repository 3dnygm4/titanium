#forms.py - help forms handing and data validation

from wtforms import Form, TextField, DateField, IntegerField, \
                        SelectField, PasswordField, validators, RadioField
                            
    
class RegisterForm(Form):
    name = TextField('Username', [validators.Required(), validators.Length(min=4,max=25)])
    email= TextField('Email', [validators.Required(), validators.Length(min=4,max=40)])
    password = PasswordField('Password',[validators.Required(),validators.Length(min=4,max=40),
                                validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password',[validators.Required(),validators.Length(min=4,max=40)])
    typ = RadioField('Type', choices=[('Manager','Manager'),('Member','Member')])

class LoginForm(Form):
    name = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])
    
