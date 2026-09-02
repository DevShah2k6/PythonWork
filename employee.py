from sqlalchemy import create_engine
from sqlalchemy.orm  import Session,sessionmaker,declarative_base
from sqlalchemy import String,Integer,Column,DateTime

Base = declarative_base()


from datetime import datetime


engine = create_engine("mysql+pymysql://root:root@localhost/Alembic_Employee_Db")
session_maker = sessionmaker(bind=engine)
session = session_maker()
class Employee(Base):
    __tablename__ = "employees"

    id  = Column(Integer,primary_key=True)
    first_name = Column(String(length=200),nullable=False)
    last_name = Column(String(length=100),nullable=False)
    department_name = Column(String(length=15),nullable=False)
    # salary = Column(Integer,nullable=False)

employees = [
    Employee(first_name = "XYZ",last_name = "ABC",department_name = "HR"),
    Employee(first_name="PQR",last_name = "KLM",department_name = "AI-ML"),
    Employee(first_name="ASD",last_name="OPO",department_name = "Marketing")
]

def save_employee():
    for emp in employees:
        session.add(emp)
        session.commit()

save_employee()




def delete_employee(id):
    employee_record = session.query(Employee).filter(Employee.id==id).first()
    session.delete(employee_record)
    session.commit()
# delete_employee(1)
