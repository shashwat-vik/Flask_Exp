from sqlalchemy import Column, Integer, Float, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 't_customers'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    number = Column(String(10), nullable=False)
    account = relationship("Account", back_populates="customer")

    def __init__(self, *args, **kwargs):
        Base.__init__(self, *args, **kwargs)

    def __repr__(self):
        return "Customer<{0}>".format(self.name)

class Account(Base):
    __tablename__ = 't_accounts'
    id = Column(Integer, primary_key=True)
    acc_no = Column(String(12), nullable=False)
    balance = Column(Float, nullable=False, default=0.0)
    cust_id = Column(Integer, ForeignKey('t_customers.id'))
    customer = relationship("Customer", back_populates="account")

    def __init__(self, *args, **kwargs):
        Base.__init__(self, *args, **kwargs)

    def __repr__(self):
        return "Account<{0}>".format(self.acc_no)

# FOR 'views.py' ------------------------------
import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine(config.Database.SQLITE_DATABASE_URL)
DBSession = sessionmaker()
Base.metadata.bind = engine
session = DBSession(bind=engine)
# ---------------------------------------------
