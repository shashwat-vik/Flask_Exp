import os, sys
sys.path.append(os.path.abspath("."))

from sqlalchemy import create_engine
from models import *
import config

if __name__ == '__main__':
    engine = create_engine(config.Database.SQLITE_DATABASE_URL)
    Base.metadata.create_all(engine)
