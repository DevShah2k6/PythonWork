import pymongo



client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["car_prediction"]
collection = db["predictions"]

def add_data(cardata,predicted_price):
        data = {
        "car_data": cardata.model_dump(),
        "predicted_price": predicted_price
        }
        collection.insert_one(data)
