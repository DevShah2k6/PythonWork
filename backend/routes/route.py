from fastapi.routing import APIRouter
from ML.prediction import predict_car
from models.model import CarPrice
from database import add_data
carprice = APIRouter()

@carprice.post("/predict")
def car_price_predict(cardata:CarPrice):
    predicted_price = predict_car(car_data=cardata)
    add_data(cardata,predicted_price)
    return predicted_price