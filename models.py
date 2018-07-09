#models.py

from app import db


#Ftasks for tasks.html
class FTasks(db.Model):
    
    __tablename__ = "ftasks"
    
    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    due_date = db.Column(db.Date, nullable = False )
    priority = db.Column(db.Integer, nullable = False)
    posted_date = db.Column(db.Date,nullable = False)
    status = db.Column(db.Integer)
    approval = db.Column(db.Boolean)
    #relationship many side
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __init__(self, name, due_date, priority, posted_date, status, user_id, approval):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.posted_date = posted_date
        self.status = status
        self.user_id = user_id
        self.approval = approval
        
    def __repr__(self):
        return '<name %r>' %(self.body)
  

#user for new user  
class User(db.Model):
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key = True )
    name = db.Column(db.String, unique = True , nullable = False)
    email= db.Column(db.String, unique = True , nullable = False)
    password = db.Column(db.String, nullable = False )
    typ = de.Column(db.String, nullable = False)
    #relationship
    tasks = db.relationship('FTasks', backref='poster')
    
    def __init__(self, name =None, email=None, password=None, typ=None):
        self.name = name
        self.email = email
        self.password = password
        self.typ = typ
        
    def __repr__(self):
        return '<User %r>' %(self.name)
        
        
 

 