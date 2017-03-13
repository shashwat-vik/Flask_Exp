import os, sys
os.chdir('../')
sys.path.append(os.path.abspath('.'))

from models import *
import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(config.Database.SQLITE_DATABASE_URL)
DBSession = sessionmaker()
Base.metadata.bind = engine
session = DBSession(bind=engine)

'''
# ADD BELOW ENTRIES IF DATABASE IS EMPTY

# ====================================================
python_blog = Blog(title="Blog on Python", body="Python Tutorials for Newbie")
flask_blog = Blog(title="Blog on Flask", body="Flask Tutorials for Newbie")
python_tag = Tag(name="Python")
flask_tag = Tag(name="Flask")

python_blog.tags = [python_tag]
flask_blog.tags = [python_tag, flask_tag]
session.add_all([python_blog, flask_blog, python_tag, flask_tag])
session.commit()
# ====================================================
'''

blogs = session.query(Blog).all()
tags = session.query(Tag).all()

print ("\n(1) Blog's backref is default, i.e.'select'. Hence loads the entry in single SQL query.")
print (repr(blogs[0].tags), end='\n\n')

print ("(2) Tag's backref is 'dynamic'. Hence return a Query Object instead.")
print (repr(tags[0].blogs))
print ("After Tag's second query we get data.")
print (repr(tags[0].blogs.all()))
