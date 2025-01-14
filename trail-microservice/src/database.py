from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'mssql+pyodbc://HBuck:KzgN819+@dist-6-505.uopnet.plymouth.ac.uk/COMP2001_HBuck?driver=ODBC+Driver+17+for+SQL+Server'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Import models to ensure they are registered with SQLAlchemy
from models import trail_model, user_model