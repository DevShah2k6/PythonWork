from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.book import route
from database import Base, engine
import models

app =FastAPI()


app.add_middleware(
    CORSMiddleware,
     allow_origins = [ "http://localhost:5173"],
    allow_credentials=True,
    allow_methods = ["*"],
    allow_headers = ["*"]    
)

Base.metadata.create_all(bind=engine)

#to include the route so tlaking to the databse is done with the help of this
app.include_router(router=route)