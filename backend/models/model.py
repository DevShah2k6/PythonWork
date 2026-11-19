from pydantic import BaseModel

class Student(BaseModel):
    name:str
    email:str
    age:str
    course:str

class StudentResponse(BaseModel):
    id:str
    name: str
    email: str
    age: str
    course: str