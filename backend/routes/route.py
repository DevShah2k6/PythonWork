from fastapi import APIRouter
from database import add_student,show_student,delete_student_record,update_Student_record
from models.model import Student,StudentResponse
student = APIRouter()

@student.post("/students")
def save_student(student_data:Student):
    add_student(student_data=student_data)
    return {"message":"Student Added Successfully"}

@student.get("/students",response_model=list[StudentResponse])
def shows_student():
   return  show_student()

@student.delete("/student/{student_id}")
def delete_student(student_id:str):
    delete_student_record(student_id)

@student.put("/students/{student_id}")
def edit_student(student_id:str,student_data:Student):
    update_Student_record(student_id=student_id,student_data=student_data)