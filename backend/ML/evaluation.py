from sklearn.metrics import r2_score,root_mean_squared_error,mean_absolute_error,mean_squared_error


def evaluate_model(y_test,y_pred,y_train,y_pred_train):
    print("---------MODEL EVALUATION----------")
    mae = mean_absolute_error(y_test,y_pred)
    mse = mean_squared_error(y_test,y_pred)
    rmse = root_mean_squared_error(y_test,y_pred)
    model_r2_score = r2_score(y_test,y_pred)
    train_r2 = r2_score(y_train, y_pred_train)
    print("Training R²:", train_r2)
    print(f"MAE:{mae}")
    print(f"MSE:{mse}")
    print(f"RMSE:{rmse}")
    print(f"Test R2 SCORE:{model_r2_score}")
    return mae,mse,rmse,model_r2_score,train_r2