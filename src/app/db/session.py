from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base  # Import Base from base.py

# Replace 'sqlite:///./test.db' with your actual database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()