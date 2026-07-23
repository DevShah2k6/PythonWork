from sqlalchemy.orm import Session
from models import Employee
from schemas import EmployeeCreate,EmployeeResponse


#creating the new employee and inserteed into database
#here the data is coming from frontend and then validation is doen and thne inserted into
#database 
def create_employee(db:Session,employee:EmployeeCreate):    
    new_employee_data = Employee(fullname=employee.fullname,age=employee.age,salary=employee.salary,desgination=employee.desgination)

    db.add(new_employee_data)
    db.commit()
    db.refresh(new_employee_data)

    return new_employee_data

#taking all employees 
def get_employees(db:Session):
    employee = db.query(Employee).all()
    return employee

#updating the employee in database
def update_employees(db:Session,eid:int,employee_name:str,age:int,salary:int,desg:str):
    employee = db.query(Employee).filter(Employee.id==eid).first()
    employee.fullname = employee_name
    employee.age = age
    employee.salary = salary
    employee.desgination = desg
    db.commit()
    db.refresh(employee)
    print("Updating:", employee.id, salary)
    return employee

#delete the data from the databse
def delete_employee(db:Session,eid:int):
    employee = db.query(Employee).filter(Employee.id==eid).first()
    print("Database employees:", employee)
    if not employee:
        return {"message":"Employee Not Found"}
    
    db.delete(employee)
    db.commit()
    return {"message":"Employee Deleted"}