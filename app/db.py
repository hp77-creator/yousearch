from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

import os

load_dotenv()

SQLALCHEMY_DB_URL = os.environ.get("DB_URL", "postgresql+psycopg2://postgres:postgres@db:5432/test")


engine = create_engine(SQLALCHEMY_DB_URL)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
