import pandas as pd
from analysis import dataset_analysis
from data_visulization import data_chart
from encoding import encodeing
from train_test_spliting import train_test_split_data
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor
from sklearn.model_selection import KFold, cross_val_score
from models import train_model,test_model
from evaluation import evaluate_model
import numpy as np
import joblib
import json
import json
from pathlib import Path
crop = pd.read_csv("../dataset/mandi_price_dataset.csv")

print(crop)
dataset_analysis(crop)
data_chart(crop)
crop = encodeing(crop)
x_train,x_test,y_train,y_test = train_test_split_data(crop)
kf = KFold(n_splits=5, shuffle=True, random_state=42)
# y_test = np.expm1(y_test)
models = {
    "Linear Regression": LinearRegression(),
    "Ridge": Ridge(max_iter=1000, random_state=42),
    "Lasso": Lasso(alpha=0.3, max_iter=1000),
    "DecisionTreeRegressor": DecisionTreeRegressor(
        max_depth=4,
        random_state=42
    ),
    "RandomForestRegressor": RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ),
    "XGBRegressor": XGBRegressor()
}
ss = StandardScaler()

x_train_scaled = ss.fit_transform(x_train)
x_test_scaled = ss.transform(x_test)

scaled_models = {
    "SVR": SVR(C=0.3,max_iter=1000),
    "KNR": KNeighborsRegressor(n_neighbors=3)
}
best_model = None
best_score = float("-inf")
best_model_name = None

for model_name, model in models.items():

    y_pred_train = train_model(
        model=model,
        x_train=x_train,
        y_train=y_train
    )

    y_pred, y_test = test_model(
        model=model,
        x_test=x_test,
        y_test=y_test
    )

    mae, mse, rmse, test_r2, train_r2 = evaluate_model(
        y_pred=y_pred,
        y_test=y_test,
        y_train=y_train,
        y_pred_train=y_pred_train
    )
    cv_scores = cross_val_score(model, x_train, y_train, cv=kf, scoring="r2")
    score = cv_scores.mean()
    print(model_name, "CV R²:", score)
    if score > best_score:
        best_score = score
        best_model = model
        best_model_name = model_name
        best_mae = mae
        best_mse = mse
        best_rmse = rmse
        best_test_r2 = test_r2
        best_train_r2 = train_r2


for model_name, model in scaled_models.items():

    y_pred_train = train_model(
        model=model,
        x_train=x_train_scaled,
        y_train=y_train
    )

    y_pred, y_test = test_model(
        model=model,
        x_test=x_test_scaled,
        y_test=y_test
    )

    mae, mse, rmse, test_r2, train_r2 = evaluate_model(
        y_pred=y_pred,
        y_test=y_test,
        y_train=y_train,
        y_pred_train=y_pred_train

    )
    cv_scores = cross_val_score(model, x_train_scaled, y_train, cv=kf, scoring="r2")
    score = cv_scores.mean()

    if score > best_score:
        best_score = score
        best_model = model
        best_model_name = model_name
        best_mae = mae
        best_mse = mse
        best_rmse = rmse
        best_test_r2 = test_r2
        best_train_r2 = train_r2


print("Best Model:", best_model_name)
print("Best CV R²:", best_score)
performance = {
    "best_model": best_model_name,
    "cv_r2": best_score,
    "train_r2": best_train_r2,
    "test_r2": best_test_r2,
    "mae": best_mae,
    "mse": best_mse,
    "rmse": best_rmse
}
performance_file = Path(__file__).resolve().parent.parent / "model_performance.json"

with open(performance_file, "w") as file:
    json.dump(performance, file, indent=4)

joblib.dump(best_model, "models/best_model.pkl")