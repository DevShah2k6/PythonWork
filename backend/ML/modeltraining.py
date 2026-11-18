from sklearn.model_selection import train_test_split

from encoding import encodeing
def model_training(car):
    car = encodeing(car)
    X = car.drop([
    "city",
    "estimated_final_price",
    "depreciation_amount",
    "resale_value_percent",
    "bargain_percent",
    "price_per_km",
    "listed_price"
], axis=1)
    print(X.columns)
    y = car["estimated_final_price"]
    x_train,x_test,y_train,y_test  = train_test_split(X,y,test_size=0.2,random_state=42)

    return x_train,x_test,y_train,y_test