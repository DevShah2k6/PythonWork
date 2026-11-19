import pymongo
from bson import ObjectId
client  = pymongo.MongoClient("mongodb://localhost:27017")

db = client["Students"]
collections = db["Student-data"]

def add_student(student_data):
    collections.insert_one(student_data.model_dump())

def show_student():
   students = collections.find({})
   return [
        {
            "id": str(student["_id"]),
            "name": student["name"],
            "email": student["email"],
            "age": student["age"],
            "course": student["course"]
        }
        for student in students
    ]

def delete_student_record(id):
    collections.delete_one({"_id":ObjectId(id)})

def update_Student_record(student_id,student_data):
    collections.update_one(
    {"_id": ObjectId(student_id)},
    {"$set": student_data.model_dump()}
)
    return {"message":"Updated Successfully"}