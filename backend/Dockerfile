FROM  python:3.12

WORKDIR /app


COPY . .


#install all depedencies
RUN pip install -r requirements.txt

EXPOSE 8000

#To run the app 
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

