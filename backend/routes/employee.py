from fastapi import APIRouter,Depends
from database import get_db
import crud
import schemas
from sqlalchemy.orm import Session
#here api router is created so when cal then in that fucntion code is exceuted
route = APIRouter()

@route.get("/employee")
def getmeployees(db:Session = Depends(get_db)):
    return crud.get_employees(db=db)

@route.post("/addemployee")
def addemployees(employee:schemas.EmployeeCreate,db:Session = Depends(get_db)):
    return crud.create_employee(db,employee)


@route.put("/editemployee/{eid}")
def editemployees(
    eid: int,
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):
    return crud.update_employees(
        db,
        eid=eid,
        employee_name=employee.fullname,
        age=employee.age,
        salary=employee.salary,
        desg=employee.desgination
    )

@route.delete("/deleteemployee/{eid}")
def deleteemployee(eid:int,db:Session=Depends(get_db)):
    return crud.delete_employee(db=db,eid=eid)