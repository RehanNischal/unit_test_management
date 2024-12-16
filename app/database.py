from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app import config

SQLALCHEMY_DATABASE_URL = config.DATABASE_URL

# Creating engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Method to create new sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()

# Method to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print("Exception: ",e)
    finally:
        db.close()
