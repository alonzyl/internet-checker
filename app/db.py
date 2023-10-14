from sqlalchemy import create_engine, Column, Integer, String, Sequence,DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Define the database connection URL
db_url = 'postgresql://postgres:Postgres1234@db:5432/InternetHealth'


# Create an engine
engine = create_engine(db_url)

# Create a base class for declarative models
Base = declarative_base()

class MyTable(Base):
    __tablename__ = 'InternetHealth'
    date = Column(DateTime,primary_key=True)
    isConnected = Column(Boolean)
    downloadSpeed = Column(Integer,default=None)

# Create tables if they don't exist
Base.metadata.create_all(engine)

def createSession():
    Session = sessionmaker(bind=engine)
    return Session()
