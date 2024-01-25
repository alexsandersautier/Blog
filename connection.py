from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

user = 'proxsis'
password = 'admiral'
host = 'localhost'
database = 'blog'

DATABASE_URL = f'postgresql://{user}:{password}@{host}/{database}'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()