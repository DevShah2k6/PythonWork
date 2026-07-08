import pandas as pd
import matplotlib.pyplot as plt
from models import build_logitstic_regression_model,build_decisiontree_classifier_model,build_random_forest_classifier_model,build_svc_model,build_multinomial_nb_model,run_model,build_linear_svc_model,build_k_neighbors_classifier_model,build_xgb_classifier_model,build_catboost_classifier_model
from evaluation import model_classfication_report,model_accuracy,model_confusion_matrix
from prediction import prediction
from preprocessingtext import preprocess_data
from preprocessingdataframe import preprocess_df
from featureengineering import vectorize
from encoded import encoding
from traintestsplit import train_test_split_data
from treeplotandfeatureimportance import plotting_tree,feature_importance_rfc,feature_importance_dtc


def main():
    news_df = pd.read_csv("BBC news dataset.csv")

    print(news_df)
    #Shwoing the first Five rows
    print(news_df.head())
    #Showing the last five rows
    print(news_df.tail())


    print(news_df.info())

    news_df_clean = preprocess_df(news_df=news_df)
    #Cetgrou column encoding 
    category= preprocess_data(news_df=news_df_clean)
    # Check category distribution here
    print(news_df_clean["Category"].value_counts())

    encoded_category, label_encoder = encoding(news_df_clean["Category"])
    # #text to numbers
    

    category_mapping={}
    #Shwoing the Lable and Category
    for label,categroy in zip(encoded_category,category):
        category_mapping[label] = categroy

    # Split raw text
    x_train, x_test, y_train, y_test = train_test_split_data(
        news_df_clean["description"],
        encoded_category
    )
    # vectorizer_descrption,vectroize_object = vectorize(news_df_description_vectroizer=news_df_clean["description"])

    # Fit TF-IDF only on training data
    x_train, vectroize_object = vectorize(x_train)

    # Transform test data
    x_test = vectroize_object.transform(x_test)
    import pickle
    pickle.dump(vectroize_object, open("vectorizer.pkl", "wb"))
    print(set(y_train))
    print(set(y_test))

    best_acc=0
    best_model = None
    # Models
    models = {
        "Logistic Regression": build_logitstic_regression_model(),
        "Decision Tree": build_decisiontree_classifier_model(),
        "Random Forest": build_random_forest_classifier_model(),
        "SVC": build_svc_model(),
        "Multinomial NB": build_multinomial_nb_model(),
        "KNN": build_k_neighbors_classifier_model(),
        "XGBoost": build_xgb_classifier_model(),
        "Linear SVC": build_linear_svc_model(),
        "CatBoost": build_catboost_classifier_model(),
    }
    for name,model in models.items():
        y_pred = run_model(model=model,x_train=x_train,y_train=y_train,x_test=x_test)
        acc = model_accuracy(y_test, y_pred)
        print(name,acc)
        print(model_classfication_report(y_test, y_pred))
        print(model_confusion_matrix(y_test, y_pred))
        plt.show()

        if acc>best_acc:
            best_acc = acc
            best_model = model


    print(name,best_model)
    user_input = input("Enter Text:-")
    print(category_mapping[prediction(best_model,[user_input])])


if __name__ == "__main__":
    main()
