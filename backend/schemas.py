from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    fullname:str
    age:int
    salary:int
    desgination:str

class EmployeeResponse(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True