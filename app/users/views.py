#views.py
#/app/users/views.py

from app import db
from flask import Blueprint, flash, redirect, render_template, request, \
                    session, url_for
from app.views import login_required, flash_errors
from forms import  RegisterForm, LoginForm
from app.models import User
from sqlalchemy.exc import IntegrityError

mod = Blueprint('users',__name__, url_prefix='/users', 
                template_folder='templates', static_folder='static')


#logout    
@mod.route('/logout/')
def logout():
    session.pop('logged_in',None)
    session.pop('user_id',None)
    flash('You are logged out.')
    return redirect (url_for('users.login'))

    
#main login    
@mod.route('/',methods=['POST','GET'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method =="POST" and form.validate():
        name = form.name.data
        password = form.password.data
        #u = User.query.filter_by(name=name,password=password).first()
        u = db.session.query(User).filter_by(name=name,password=password).first()
        if u is None:
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            session['user_id'] = u.id
            flash('You are logged in.')
            return redirect(url_for('tasks.tasks'))
    return render_template('/login.html', form=LoginForm(request.form),error=error)
    
#for new user to register
@mod.route('/register/', methods=['GET','POST'])
def register():
    error = None
    form = RegisterForm(request.form)

    #typs = ['Manager', 'Member']

    if form.validate():
        new_user = User(
                form.name.data,
                form.email.data,
                form.password.data,
                form.typ.data
                )
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Thanks for registering. Please login.')
            return redirect(url_for('.login'))
        except IntegrityError:
            error = 'Sorry! That username and/or email already exist. Please try again.'
    else:
        if request.method == "POST" :
            flash_errors(form)    
    return render_template('/register.html', form = form, error=error, typs = ['Manager', 'Member'])
    
    
    