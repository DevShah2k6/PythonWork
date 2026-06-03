from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class BMI(BaseModel):
    weight : int
    height : int

#when we call api it send the all details methods and cookie and etc to the request obejct which 
#is made of Request class and that object conatins all request details and
#this is pass to the request object which is written in parenthesis
#using the request 
@app.get("/")
async def get_input_data(request:Request):
    #here all request details like http method and cookie header and all that 
    #is passed in left side request varibale and then ot the html page 
    #it goes to the template engine
    #Browser → FastAPI → Request object → JinjaTemplate → HTML → Browser
    return templates.TemplateResponse(name = "input.html",request  = request)


bmi_data = []
@app.post("/result")

async def data_send(bmi:BMI):
    #here in parenthesis bmi:BMI is a pydantic class so
    #with the help of . wee can access the varible and check the datatypoe also
    result = bmi.weight/(bmi.height**2)
    print(result)
    return {"msg":"BMI Value = ","data":result}

