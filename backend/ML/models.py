import numpy as np

def train_model(model,x_train,y_train):
    model.fit(x_train,y_train)
    y_train_pred = model.predict(x_train)
    return y_train_pred

def test_model(model,x_test,y_test):
    y_pred = model.predict(x_test)
    return y_pred,y_test