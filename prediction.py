import pickle
def prediction(model,input_text):
    """
    Predicts the category of new text input.

    The text is converted into numerical features using the vectorizer
    and then passed to the trained model for prediction.
    """
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    x_input_vectorizer = vectorizer.transform(input_text)
    y_pred_user_input = model.predict(x_input_vectorizer)
    return y_pred_user_input[0]