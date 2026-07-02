from fastapi import FastAPI,Request
#from routes.note import note
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
from pydantic import BaseModel,Field
app = FastAPI()
templates = Jinja2Templates(directory="templates")
#here filed used for the datavalidation here age must be greater than 0
#pydantic c;ass student is made for validationa dn checking datatype
#hhtpexception used for to shopw the err message like id not foudn then 404 not found

class Student(BaseModel):
    student_id : int
    name : str
    age: int = Field(gt=0)
    marks : int
    course : str

student_data = []
student_id = []
students_data = []
@app.post("/students")
async def get_student_data(student:Student):
    #model_dump()->converet the object(pydantic) into python dictionary
    student_data.append(student.model_dump())
    #new_data = pd.DataFrame({"id":student.student_id,"name":student.name,"age":student.age,"marks":student.marks,"course_name":student.course})
    #orient = record -> convert the dataframe row into dictionay each
    #into dictionary
    # if student.age>100:
    #     return{"mesg":"Age not greater than 100"}
    # if student.marks>100:
    #     return {"warn":"marks should not be greater than 100"}
    
    return {"msg":"Data Added Successfully"}
    
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="student.html"
    )
@app.get("/seedata")
async def see_student_data(request :Request):
    #here data is return in form of json as student data has data so 
    
    # return templates.TemplateResponse(
    #     request=request,
    #     name="data.html",
    #     context = {"data":student_data}
    # ) 
    print(student_data)
    return {"data":student_data}
@app.get("/deletedata")
async def deletedata(request:Request):      
    return templates.TemplateResponse(
        request=request,
        name="delete.html",
        ) 
#here in below code from frontend it comes below line and then goes into the parenthesis 
#and it work
#here student_id and new marks are path paramter 

# 👉 If the route does NOT have {}
# 👉 and the parameter is only in the function

# ✔ THEN it is a Query Parameter
@app.patch("/update/{student_id}/{new_marks}")
async def update_data(student_id : int,new_marks:int):
    print("--------")
    for i in range(len(student_data)):
        if student_id == student_data[i]["student_id"]:
            print(student_data[i])
            student_data[i]["marks"] = new_marks
            return {"msg":"Updated Sucessfully","data":student_data}
    else:
     return {"msg":"Not Found"}
@app.get("/updatedata")
async def update_file(request:Request):
     return templates.TemplateResponse(
        request=request,
        name="update.html"
    )

@app.delete("/deletedata/{student_id}")
async def delete_data(student_id:int):
    print(student_data)
    for i in range(len(student_data)):
         if student_id == student_data[i]["student_id"]:
             student_data.remove(student_data[i])
             #print("after deleteing\n",student_data)
             return {"msg":"Delete Successfully"}
    return {"msg":"Not found"}
# else:
#     return {"msg":"Not found"}