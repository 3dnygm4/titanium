#flasktaskr_test.py

import os
import unittest

from app import app,db
from app.models import User
from config import basedir

TEST_DB= 'test.db'

class AddUser(unittest.TestCase):

    #this is a special method that is executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                        os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()
        
    #this is a special method that is executed after each test
    def tearDown(self):
        db.drop_all()
        
    #each test should start with 'test'
    def test_user_setup(self):
        new_user = User('mherman','mimic@mimi.org','mimimherman')
        db.session.add(new_user)
        db.session.commit()
        
if __name__ =="__main__":
    unittest.main()
        