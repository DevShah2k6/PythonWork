from sklearn.preprocessing import LabelEncoder
def encoding(news_df_category):
    """
    Encodes categorical labels into numerical values.

    This function converts text categories into numbers so that
    machine learning models can understand and process them.
    """
    le = LabelEncoder()
    encoded_category = le.fit_transform(news_df_category)
    return encoded_category,le