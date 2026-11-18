from fastapi.routing import APIRouter
from ML.prediction import crop_price_predict
from models.pydantic_models import CropPrediction
from database import insert_crop_data
import pandas as pd
from routes.model_performace import get_model_performance
crop = APIRouter()


@crop.post("/predict")
def predict_crop_price(crop_data:CropPrediction):
    predicted_price,price_per_kg = crop_price_predict(crop_data=crop_data)
    insert_crop_data(crop_data=crop_data,predicted_price=predicted_price,price_per_kg=price_per_kg)
    return {"predicted_price": predicted_price,"predicted_price_per_kg":price_per_kg}

@crop.get("/districts")
def get_districts(state: str):
    crop_data = pd.read_csv("dataset/mandi_price_dataset.csv")

    districts = (
        crop_data[crop_data["State"] == state]["District"]
        .dropna()
        .unique()
        .tolist()
    )

    return {"districts": districts}

@crop.get("/markets")
def get_markets(state: str, district: str):
    crop_data = pd.read_csv("dataset/mandi_price_dataset.csv")

    markets = (
        crop_data[
            (crop_data["State"] == state) &
            (crop_data["District"] == district)
        ]["Market"]
        .dropna()
        .unique()
        .tolist()
    )

    return {"markets": markets}

@crop.get("/states")
def get_states():
    crop_data = pd.read_csv("dataset/mandi_price_dataset.csv")

    states = (
        crop_data["State"]
        .dropna()
        .unique()
        .tolist()
    )

    return {"states": states}
@crop.get("/commodities")
def get_commodities(state: str, district: str, market: str):
    crop_data = pd.read_csv("dataset/mandi_price_dataset.csv")

    commodity = (
        crop_data[
            (crop_data["State"] == state) &
            (crop_data["District"] == district) &
            (crop_data["Market"] == market)
        ]["Commodity"]
        .dropna()
        .unique()
        .tolist()
    )

    return {"commodities": commodity}

@crop.get("/variety")
def get_commodities(state: str, district: str, market: str,commodity:str):
    crop_data = pd.read_csv("dataset/mandi_price_dataset.csv")

    variety = (
        crop_data[
            (crop_data["State"] == state) &
            (crop_data["District"] == district) &
            (crop_data["Market"] == market) &
            (crop_data["Commodity"] == commodity)
        ]["Variety"]
        .dropna()
        .unique()
        .tolist()
    )

    return {"varieties": variety}

@crop.get("/grades")
def get_grades(
    state: str,
    district: str,
    market: str,
    commodity: str,
    variety: str
):
    crop_data = pd.read_csv("dataset/mandi_price_dataset.csv")

    grade = (
        crop_data[
            (crop_data["State"] == state) &
            (crop_data["District"] == district) &
            (crop_data["Market"] == market) &
            (crop_data["Commodity"] == commodity) &
            (crop_data["Variety"] == variety)   
        ]["Grade"]
        .dropna()
        .unique()
        .tolist()
    )

    return {"grades": grade}


@crop.get("/model-performance")
def model_performance_score():
    return get_model_performance()