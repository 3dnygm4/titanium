#views.py
#/app/tasks/views.py

from app import app, db
from flask import Blueprint, flash, redirect, render_template, request, \
                    session, url_for
from app.views import login_required, flash_errors
from forms import AddTask
from app.models import FTasks
from app.models import User

mod = Blueprint('tasks',__name__, url_prefix='/tasks',template_folder='templates',
                static_folder = 'static')


@login_required



#Task fetch all from db    
@mod.route('/tasks/')
@login_required
def tasks():
    typ = User.query.filter_by(id=session['user_id']).first()
    approval_tasks = db.session.query(FTasks).filter_by(approval='0').order_by(FTasks.priority.desc())
    open_tasks = db.session.query(FTasks).filter_by(status='1').order_by(FTasks.priority.desc())
    closed_tasks = db.session.query(FTasks).filter_by(status='0').order_by(FTasks.priority.desc())
    return render_template('/tasks.html',form = AddTask(request.form),
            open_tasks=open_tasks, closed_tasks = closed_tasks, approval_tasks = approval_tasks, typ = typ.typ)


#Add new tasks:
@mod.route('/add/',methods=['POST','GET'])
@login_required
def new_task():
    form = AddTask(request.form)
    typ = User.query.filter_by(id=session['user_id']).first()
    approval = '0'
    status = '-1'

   

    if typ.typ == 'Manager':
        approval = '1'
        status = '1'
    

    if form.validate():
        new_task = FTasks(
                    form.name.data,
                    form.due_date.data,
                    form.priority.data,
                    form.posted_date.data,
                    status,
                    session['user_id'],
                    approval
                    )
        db.session.add(new_task)
        db.session.commit()
        flash('New entry was successfully posted. Thanks.')
    else:
        flash_errors(form)
    return redirect(url_for('.tasks'))

        
#Mark tasks as complete:
@mod.route('/complete/<int:task_id>/',)
@login_required
def complete(task_id):
    new_id = task_id
    db.session.query(FTasks).filter_by(task_id=new_id).update({"status":"0"})
    db.session.commit()
    flash('The task was marked as complete. Nice.')
    return redirect(url_for('.tasks'))
    

#Delete Tasks:
@mod.route('/delete/<int:task_id>/',)
@login_required
def delete_entry(task_id):
    new_id = task_id
    db.session.query(FTasks).filter_by(task_id=new_id).delete()
    db.session.commit()
    flash('The task was deleted. Why not add a new one?')
    return redirect(url_for('.tasks'))

    
#Incomplete the closed tasks:
@mod.route('/incomplete/<int:task_id>/',)
@login_required
def uncomplete(task_id):
    new_id = task_id
    db.session.query(FTasks).filter_by(task_id=new_id).update({'status':'1'})
    db.session.commit()
    flash('The task was marked as incomplete.')
    return redirect(url_for('.tasks'))


#Task Approval
@mod.route('/approve/<int:task_id>/',)
@login_required
def approve(task_id):
    new_id = task_id
    db.session.query(FTasks).filter_by(task_id=new_id).update({'status':'1'})
    db.session.query(FTasks).filter_by(task_id=new_id).update({'approval':'1'})

    db.session.commit()
    flash('The task was marked as incomplete.')
    return redirect(url_for('.tasks'))    
    

    
    