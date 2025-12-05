from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base

DATABASE_URL = "sqlite:///tikiti.db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
