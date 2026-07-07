import pickle

vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
def prediction(model,input_text):
    x_input_vectorizer = vectorizer.transform(input_text)
    y_pred_user_input = model.predict(x_input_vectorizer)
    return y_pred_user_input[0]