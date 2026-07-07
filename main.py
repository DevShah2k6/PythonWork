import pandas as pd
import matplotlib.pyplot as plt
import spacy
from models import LogitsticregressionModel,DecisionTreeclassfierModel,RandomForestclassfierModel,SVCModel,MutinomialNBModel,run_model,LinearSvcModel,KNeighboursclassifierModel,XgbclassifierModel,CatBoostclassiferModel
from errormetrics import model_classfication_report,model_accuracy,model_confusion_matrix
from prediction import prediction
from preprocessingtext import preprocess_data
from preprocessingdataframe import preproces_df
from featureengineering import vectorize
from encoded import encoding
from traintestsplit import train_test_split_data
from treeplotandfeatureimportance import plotting_tree,feature_importance_rfc,feature_importance_dtc
nlp = spacy.load("en_core_web_sm")
# nlp = spacy()

news_df = pd.read_csv("BBC news dataset.csv")

print(news_df)
#Shwoing the first Five rows
print(news_df.head())
#Showing the last five rows
print(news_df.tail())


print(news_df.info())

news_df_clean = preproces_df(news_df=news_df)
print("-------\n",news_df_clean)
#Cetgrou column encoding 
category= preprocess_data(news_df=news_df_clean)
# print("++++++\n",category)
encoded_categroy = encoding(news_df_category=category)
# print(encoded_categroy)
# #text to numbers

vectorizer_descrption,vectroize_object = vectorize(news_df_description_vectroizer=news_df_clean["description"])
import pickle
pickle.dump(vectroize_object, open("vectorizer.pkl", "wb"))

category_mapping={}
#Shwoing the Lable and Category
for label,categroy in zip(encoded_categroy,category):
    category_mapping[label] = categroy

#Training and Testing and splitng Data
x_train,x_test,y_train,y_test = train_test_split_data(vectorizer_descrption,encoded_categroy)
print("Done")

# Models
model = LogitsticregressionModel()
y_pred = run_model(model,x_train=x_train,y_train=y_train,x_test=x_test)
print(model_accuracy(y_test,y_pred))
print(model_confusion_matrix(y_true=y_test,y_pred=y_pred))
print(model_classfication_report(y_true=y_test,y_pred=y_pred))
plt.show()

#here i had used the Logistic Regression object in dtf so 
# # it follows the lsp principle
model = DecisionTreeclassfierModel()
y_pred_dtc = run_model(model,x_train=x_train,y_train=y_train,x_test=x_test)
print(model_accuracy(y_test,y_pred_dtc))
print(model_classfication_report(y_true=y_test,y_pred=y_pred_dtc))
print(model_confusion_matrix(y_true=y_test,y_pred=y_pred_dtc))
plt.show()
plotting_tree(model=model)
# feature_importance_dtc(model,vectorizer=vectroize_object)

rfc = RandomForestclassfierModel()
y_pred_rfc = run_model(rfc,x_train=x_train,y_train=y_train,x_test=x_test)
print(model_accuracy(y_test,y_pred_rfc))
print(model_classfication_report(y_true=y_test,y_pred=y_pred_rfc))
print(model_confusion_matrix(y_true=y_test,y_pred=y_pred_rfc))

svc = SVCModel()
y_pred_svc = run_model(svc,x_train=x_train,y_train=y_train,x_test=x_test)

print(model_accuracy(y_test,y_pred_svc))
print(model_classfication_report(y_true=y_test,y_pred=y_pred_svc))
print(model_confusion_matrix(y_true=y_test,y_pred=y_pred_svc))


mnb = MutinomialNBModel()

y_pred_mnb = run_model(mnb,x_train=x_train,y_train=y_train,x_test=x_test)
print(model_accuracy(y_test,y_pred_mnb))
print(model_classfication_report(y_true=y_test,y_pred=y_pred_mnb))
print(model_confusion_matrix(y_true=y_test,y_pred=y_pred_mnb))

# #KNN
knn = KNeighboursclassifierModel()

y_pred_knn = run_model(knn,x_train=x_train,y_train=y_train,x_test=x_test)
print(model_accuracy(y_test,y_pred_knn))
print(model_classfication_report(y_true=y_test,y_pred=y_pred_knn))
print(model_confusion_matrix(y_true=y_test,y_pred=y_pred_knn))

num_classes = len(set(y_train))
xgb = XgbclassifierModel(num_classes=num_classes)
y_pred_xgb = run_model(knn,x_train=x_train,y_train=y_train,x_test=x_test)

print(model_accuracy(y_test,y_pred_xgb))
print(model_classfication_report(y_true=y_test,y_pred=y_pred_xgb))
print(model_confusion_matrix(y_true=y_test,y_pred=y_pred_xgb))

# LinearSVC
lsvc = LinearSvcModel()

y_pred_lsvc = run_model(lsvc,x_train=x_train,y_train=y_train,x_test=x_test)
print(model_accuracy(y_test,y_pred_lsvc))
print(model_classfication_report(y_true=y_test,y_pred=y_pred_lsvc))
print(model_confusion_matrix(y_true=y_test,y_pred=y_pred_lsvc))

#CatBoostClassifer
cbc = CatBoostclassiferModel()

y_pred_cbc = run_model(cbc,x_train=x_train,y_train=y_train,x_test=x_test)
print(model_accuracy(y_test,y_pred_cbc))
print(model_classfication_report(y_true=y_test,y_pred=y_pred_cbc))
print(model_confusion_matrix(y_true=y_test,y_pred=y_pred_cbc))
user_input = input("Enter Text:-")
# print(category_mapping[prediction(lsvc,["India defeated Australia in the final match yesterday. Rohit Sharma scored a century and led the team to victory."])])
print(category_mapping[prediction(lsvc,[user_input])])



