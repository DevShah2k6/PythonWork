

# from encoding import encodeing
import joblib
import numpy as np

import pandas as pd
best_model = joblib.load("ML/models/best_model.pkl")
encoder = joblib.load("ML/models/encoder.pkl")
def crop_price_predict(crop_data):
    categorical_data = pd.DataFrame([[
        crop_data.State,
        crop_data.District,
        crop_data.Market,
        crop_data.Commodity,
        crop_data.Variety,
        crop_data.Grade
    ]], columns=[
        "State",
        "District",
        "Market",
        "Commodity",
        "Variety",
        "Grade"
    ])
    encoded_data = encoder.transform(categorical_data)
    
    encoded_df = pd.DataFrame(
        encoded_data.toarray(),
        columns=encoder.get_feature_names_out()
    )

    final_crop_data = pd.concat([encoded_df], axis=1)
    prediction = best_model.predict(final_crop_data)
    prediction = np.expm1(prediction)
    price_per_kg = round(prediction[0],2) / 100
    return round(prediction[0],2),price_per_kg