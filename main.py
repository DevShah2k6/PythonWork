import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC  
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from xgboost import XGBClassifier
titanic = pd.read_csv("Titanic-Dataset.csv")
print(titanic)
#Checking the shape
print(titanic.shape)
#Checking the nullm values
print(titanic.isnull().sum())
#checking duplicated values
print(titanic.duplicated().sum())
# adult.drop_duplicates(inplace=True)
# print(adult.duplicated().sum())
# #checking for ? in dataset
# print(adult[adult=="?"].sum())
print(int(titanic["Age"].mean()))
titanic["Age"] = titanic["Age"].fillna(int(titanic["Age"].mean()))
# adult.fillna(adult["workclass"].mode(),inplace=True)
print(titanic.isnull().sum())

print(titanic["Embarked"].mode())
mode_embark = titanic["Embarked"].mode()
#here pandas expect the dict in form of ({"col_name":values to fill})
titanic.fillna({"Embarked": mode_embark[0]}, inplace=True)
print(titanic.isnull().sum())

print(titanic["Cabin"].mode())

titanic.fillna({"Cabin":"Unknown"},inplace=True)
print(titanic.isnull().sum())
print(titanic.describe().T)
print(titanic.info())
#titanic["Cabin"] = titanic["Cabin"].map({"Unknown":0})

sns.countplot(titanic["Sex"])
plt.xlabel("Count of Male and Female")
plt.ylabel("Gender")
plt.title("Gender vs Count of Male and Female")
plt.show()


print(titanic["Survived"].value_counts(normalize=True)*100)
survived = titanic["Survived"].value_counts(normalize=True)*100
plt.pie(survived.values,labels=survived.index,autopct="%1.1f%%")
plt.title("Pie Chart of Survived (Target Feature)")
plt.show()

embark = titanic["Embarked"].value_counts(normalize=True)*100
plt.pie(embark.values,labels=embark.index,autopct="%1.1f%%")
plt.title("Pie Chart of Embark")
plt.show()
print(embark)

titanic["Embarked"]= titanic["Embarked"].map({"S":10,"C":51,"Q":21})
print(titanic["Embarked"])
titanic["Sex"]= titanic["Sex"].map({"male":0,"female":1})
print(titanic["Sex"])
print(titanic["Cabin"].nunique())

titanic["Cabin"] = titanic["Cabin"]
print(titanic["Cabin"].str[0].value_counts())
print(titanic["Cabin"])

#titanic["Cabin"] = pd.get_dummies(titanic,columns=["Cabin"])

x = titanic[["Pclass","Sex","Age","SibSp","Parch","Fare","Embarked","Cabin"]]
y = titanic["Survived"]
x = pd.get_dummies(x,columns=["Cabin"])
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.30,random_state=42)

loreg = LogisticRegression(max_iter=600,random_state=42)
loreg.fit(x_train,y_train)

y_pred = loreg.predict(x_test)
print(accuracy_score(y_test,y_pred))
sns.heatmap(confusion_matrix(y_pred,y_test),cmap="coolwarm",annot=True)
plt.title("Heatmap of Confusion Matrix of Logistic Regression")
plt.show()
#model_acc_score = pd.DataFrame({"LogisticRegression":accuracy_score})
 
dtc = DecisionTreeClassifier(max_depth=4,min_samples_leaf=3,min_samples_split=3,random_state=42)
dtc.fit(x_train,y_train)

y_pred_dtc = dtc.predict(x_test)
print(classification_report(y_test,y_pred_dtc))
tree.plot_tree(dtc)
plt.show()

sns.heatmap(confusion_matrix(y_pred_dtc,y_test),cmap="coolwarm",annot=True)
plt.title("Heatmap of Confusion Matrix of DecisionTreeClassifier")
plt.show()
#print(dtc.feature_importances_)
#plt.bar(x.columns,dtc.feature_importances_)
#plt.show()
rfc = RandomForestClassifier(max_depth=4,n_estimators=200,random_state=42)
rfc.fit(x_train,y_train)

y_pred_rfc = rfc.predict(x_test)
print(classification_report(y_test,y_pred_rfc))

sns.heatmap(confusion_matrix(y_pred_rfc,y_test),cmap="Blues",annot=True)
plt.title("Heatmap of Confusion Matrix of RandomForestClassifier")
plt.show()
#it finds the hyperplane and then it classoify points and at time of prediction it sess
#hwich point bleong to which class 
svc = SVC(C=0.5,kernel="linear",max_iter=500)
svc.fit(x_train,y_train)

y_pred_svc = svc.predict(x_test)
print(classification_report(y_test,y_pred_svc))

sns.heatmap(confusion_matrix(y_pred_svc,y_test),cmap="coolwarm",annot=True)
plt.title("Heatmap of Confusion Matrix of SupportVectorClassifier")
plt.show()
#guassinanb is used as age pclass and all that continous data
gnb = GaussianNB(var_smoothing=1e-10)
gnb.fit(x_train,y_train)

y_pred_gnb = gnb.predict(x_test)
print(classification_report(y_pred_gnb,y_test))

sns.heatmap(confusion_matrix(y_pred_gnb,y_test),cmap="YlOrRd",annot=True)
plt.title("Heatmap of Confusion Matrix of GuassianNaivesBayes")
plt.show()

knc = KNeighborsClassifier(n_neighbors=5,algorithm="brute",metric="euclidean")
knc.fit(x_train,y_train)
y_pred_knc = knc.predict(x_test)
print(classification_report(y_pred_knc,y_test))

sns.heatmap(confusion_matrix(y_pred_knc,y_test),cmap="Purples",annot=True)
plt.title("Heatmap of Confusion Matrix of KnearestNeighbour")
plt.show()

xgb = XGBClassifier(n_estimators=300,max_depth=4,random_state=42)
xgb.fit(x_train,y_train)
y_pred_xgb = xgb.predict(x_test)
print(classification_report(y_pred_xgb,y_test))

sns.heatmap(confusion_matrix(y_pred_xgb,y_test),cmap="coolwarm",annot=True)
plt.title("Heatmap of Confusion Matrix of XGBoost")
plt.show()
#user input

pclass = int(input("Enter 1,2,3:-"))
gender = int(input("Enter 0 (male) and 1(female):-"))
age = int(input("Enter Age:-"))
sibsp = int(input("Enter No of Sibling and Spouse:-"))
parch = int(input("Enter No of Parents and Children:-"))
fare = int(input("Enter Fare:-"))
cabin = input("Enter A/B/C/U:-")
embarked = int(input("Enter 10 for S 51 for C 21 for Q:-"))

user_df = pd.DataFrame({
    "Pclass":[pclass],
    "Gender":[gender],
    "Age":[age],
    "SibSp":[sibsp],
    "Parch":[parch],
    "Fare":[fare],
    "Cabin":[cabin],
    "Embark":[embark]
})

user_df = pd.get_dummies(user_df,columns=["Cabin"])

user_df = user_df.reindex(columns=x.columns, fill_value=0)

output = loreg.predict(user_df)
print(output)

if output==0:
    print("Not Survived")
else:
    print("Survived")