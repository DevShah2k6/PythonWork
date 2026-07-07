from sklearn.preprocessing import LabelEncoder
def encoding(news_df_category):
    le = LabelEncoder()
    encoded_category = le.fit_transform(news_df_category)
    return encoded_category