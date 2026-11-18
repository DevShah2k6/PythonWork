import joblib
import pandas as pd

model = joblib.load("ML/saved_models/model.pkl")
encoder = joblib.load("ML/saved_models/encoder.pkl")
def predict_car(car_data):
    categorical_data = [[
        car_data.fuelType,
        car_data.transmission,
        car_data.brand,
        car_data.model,
        car_data.ownerType
    ]]
    premium = 1 if car_data.premiumCar == "Yes" else 0
    numeric_df = pd.DataFrame([[
    car_data.year,
    car_data.kmDriven,
    car_data.mileage,
    car_data.engineCC,
    car_data.conditionRating,
    car_data.originalPrice,
    car_data.daysToSell,
    car_data.carAge,
    car_data.demandScore,
    car_data.brandPopularityScore,
    premium
]], columns=[
    "year",
    "km_driven",
    "mileage",
    "engine_cc",
    "condition_rating",
    "original_price",
    "days_to_sell",
    "car_age",
    "demand_score",
    "brand_popularity_score",
    "premium_car"
])

    encoded_data = encoder.transform(categorical_data)
    encoded_df = pd.DataFrame(
    encoded_data,
    columns=encoder.get_feature_names_out()
)
    
    final_car_data = pd.concat([numeric_df,encoded_df],axis=1)
    prediction = model.predict(final_car_data)
    return int(prediction[0])