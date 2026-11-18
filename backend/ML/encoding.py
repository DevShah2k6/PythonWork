from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import joblib


def encodeing(crop):

    categorical_columns = [
        "State",
        "District",
        "Market",
        "Commodity",
        "Variety",
        "Grade"
    ]

    encoder = OneHotEncoder(
        handle_unknown="ignore"
    )

    encoded_data = encoder.fit_transform(
        crop[categorical_columns]
    )

    joblib.dump(
        encoder,
        "models/encoder.pkl"
    )

    encoded_df = pd.DataFrame(
        encoded_data.toarray(),
        columns=encoder.get_feature_names_out(categorical_columns),
        index=crop.index
    )

    crop = crop.drop(
        columns=categorical_columns
    )

    crop = pd.concat(
        [crop, encoded_df],
        axis=1
    )

    return crop