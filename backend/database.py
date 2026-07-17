from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

DATABASE_URL = "sqlite:///./employee.db"

#CONNECTING THE fast api to the engine 
engine  = create_engine(DATABASE_URL,connect_args={"check_same_thread":False})


#creating the session 
SessionLocal = sessionmaker(autocommit = False,autoflush=False,bind=engine)


#the class which inheorts the another class 
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()