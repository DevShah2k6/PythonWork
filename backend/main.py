from fastapi import FastAPI,middleware
from fastapi.middleware.cors import CORSMiddleware
from routes.employee import route
from database import Base, engine
import models
app = FastAPI()

#here flow -> main.py->employee.py->model.py & schemas.py->database.py (to talk with databse)

# CORS middleware is used to allow frontend requests,
# HTTP methods, headers, and credentials like cookies/auth tokens.
app.add_middleware(
    CORSMiddleware,
    allow_origins = [ "http://localhost:5173"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

Base.metadata.create_all(bind=engine)

app.include_router(route)