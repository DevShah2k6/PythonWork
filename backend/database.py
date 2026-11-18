import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client["Crop"]
collection = database["crop-price"]

def insert_crop_data(crop_data,predicted_price,price_per_kg):
    data = {"crop_data":crop_data.model_dump(),
            "predicted_price":predicted_price,
            "Price_Per_kg":price_per_kg}
    collection.insert_one(data)