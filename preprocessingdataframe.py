

def preprocess_df(news_df):
    """
    Cleans and preprocesses the input DataFrame by handling missing values
    and preparing the data for further text processing.
    """
    print(news_df.isnull().sum())


    #Dropping the null values
    news_df.dropna(inplace=True)

    print(news_df.isnull().sum())
    

    return news_df