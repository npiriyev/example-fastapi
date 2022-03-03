
from cgitb import text
from sqlalchemy import TIMESTAMP, Column, String, Integer,Boolean
from sqlalchemy.sql.expression import text
from .database import Base

class Posts(Base):
    __tablename__='posts'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(50), nullable=False)
    owner = Column(String(20), nullable=False)
    created_time = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

class Users(Base):
    __tablename__='users'

    id = Column(Integer, primary_key=True, nullable=False)
    email=Column(String(60), nullable=False, unique=True)
    password=Column(String, nullable=False)
    created_at=Column(TIMESTAMP(timezone=True), server_default=text('now()'))