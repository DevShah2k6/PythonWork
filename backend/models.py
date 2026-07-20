
from sqlalchemy import Column, Integer, String
from database import Base
class Book(Base):
     __tablename__ ="books"

     id = Column(Integer, primary_key=True, index=True)
     bookname = Column(String)
     authorname = Column(String)
     category = Column(String)
     quantity = Column(Integer)