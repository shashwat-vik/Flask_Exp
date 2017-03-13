import os, sys
os.chdir('../')
sys.path.append(os.path.abspath('.'))

from sqlalchemy import create_engine
import models
import config

if __name__ == '__main__':
    engine = create_engine(config.Database.SQLITE_DATABASE_URL)
    models.Base.metadata.create_all(engine)
