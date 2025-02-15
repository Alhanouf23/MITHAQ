from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL 
DATABASE_URL = "mysql+pymysql://username:password@localhost/mangmentDB"  

# Creating engine and sessionmaker
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Test Database Connection
try:
    # Try connecting to the database
    connection = engine.connect()
    print("Database connected successfully!")
except OperationalError as e:
    print(f"Error connecting to the database: {e}")
finally:
    if 'connection' in locals():
        connection.close()

#  Use the session FastAPI 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
