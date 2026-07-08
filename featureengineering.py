from sklearn.feature_extraction.text import TfidfVectorizer
#as object is returning because in this the learning feature are there as cricket-- column0 like that
# so this is important so returning to the main.py file
def vectorize(news_df_description_vectroizer):
    """
    Converts the preprocessed text descriptions into TF-IDF feature vectors
    for training and testing machine learning models.
    """
    vectorizer = TfidfVectorizer()
    vectroizer_description = vectorizer.fit_transform(news_df_description_vectroizer)
    return vectroizer_description,vectorizer


