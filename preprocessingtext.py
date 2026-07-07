import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess_data(news_df):
    #enabling the string operations and then splitting it and then taking the first element from it
    news_df["Category"] = news_df["tags"].str.split(",").str[0]

    print(news_df["Category"])
    print(news_df.columns)
    news_df.drop(['Unnamed: 0','tags'],axis=1,inplace=True)
    print(news_df.columns)

    #Tokenization

    # news_df["tokens"] = [[token.text for token in docs]for docs in doc ]
    # print(news_df["tokens"])



    #here pip fucntion makes the tokization process fatser by readinng multiple sentences at a time 
    doc = nlp.pipe(news_df["description"])

    print(news_df["Category"].nunique())
    print(news_df["Category"].value_counts().head(20))
    news_df["tokens"] = [[token.text for token in docs]for docs in doc ]
    print(news_df["tokens"])

    return news_df["Category"]