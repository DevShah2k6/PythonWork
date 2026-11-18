from sklearn.linear_model import LinearRegression,Ridge,Lasso
import joblib

def train_model(model, x_train, y_train):
    model.fit(x_train,y_train)
    y_train_pred = model.predict(x_train)
    return y_train_pred

def predict_model(model, x_test,y_test):
        y_pred_model = model.predict(x_test)
        return y_pred_model,y_test



