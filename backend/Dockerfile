#Use the official Python 3.12 Docker image from Docker Hub as the base image.
FROM python:3.12


#maklign the conatiner in app folder
WORKDIR /app

#copying all files and all things
COPY . . 

#install all depedencies
RUN pip install -r requirements.txt

EXPOSE 8000
#CMd means to reun that app here fastapi so these command is there
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
