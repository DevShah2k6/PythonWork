

def preproces_df(news_df):
    print(news_df.isnull().sum())

    print(news_df[news_df.isnull().head()])

    #Dropping the null values
    news_df.dropna(inplace=True)

    print(news_df.isnull().sum())
    

    return news_df