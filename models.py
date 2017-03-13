import datetime, re
from sqlalchemy import Table, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def slugify(s):
    return re.sub('[^\w]+', '-', s).lower()

association_table = Table('association_table', Base.metadata,
                        Column('tag_id', Integer, ForeignKey('tags_table.id')),
                        Column('entry_id', Integer, ForeignKey('blogs_table.id'))
                        )

class Blog(Base):
    __tablename__ = 'blogs_table'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    slug = Column(String(100), unique=True)
    body = Column(Text)
    created_timestamp = Column(DateTime, default=datetime.datetime.now)
    modified_timestamp = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    tags = relationship("Tag", secondary=association_table, backref=backref('blogs', lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        Base.__init__(self, *args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        self.slug = ''
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return "Blog({0})".format(self.title)

class Tag(Base):
    __tablename__ = 'tags_table'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    slug = Column(String(64), unique=True)

    def __init__(self, *args, **kwargs):
        Base.__init__(self, *args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return "Tag({0})".format(self.name)
