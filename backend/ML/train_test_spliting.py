from sklearn.model_selection import train_test_split
import numpy as np


def train_test_split_data(crop):

    X = crop.drop(
        columns=["Modal_x0020_Price", "Min_x0020_Price", "Max_x0020_Price", "Arrival_Date"]
    )

    y = np.log1p(crop["Modal_x0020_Price"])
    print(X.columns)

    x_train, x_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.3,
            random_state=42
        )

    return x_train, x_test, y_train, y_test