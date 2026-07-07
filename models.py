from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC,LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from encoded import encoding
from errormetrics import model_classfication_report,model_accuracy,model_confusion_matrix
#here it follows the o->open for extensiona dn closed for chnaging the code 
#foloows the solid principle

def LogitsticregressionModel():
    loreg = LogisticRegression(max_iter=300,random_state=42)
    return loreg
def DecisionTreeclassfierModel():
     dtc = DecisionTreeClassifier(max_depth=22,random_state=42,min_samples_leaf=4)
     return dtc
def RandomForestclassfierModel():
     rfc = RandomForestClassifier(n_estimators=1000,max_depth=25,random_state=42)
     return rfc

def SVCModel():
     svc  = SVC(C=0.3,random_state=42)
     return svc
def MutinomialNBModel():
     mnb = MultinomialNB()
     return mnb
def KNeighboursclassifierModel():
     knn = KNeighborsClassifier(n_neighbors=5)
     return knn
def XgbclassifierModel(num_classes):
     xgb = XGBClassifier(objective="multi:softmax", num_class=num_classes)
     return xgb

def LinearSvcModel():
     lsvc = LinearSVC(C=0.2,random_state=42,max_iter=1000)
     return lsvc
 
def CatBoostclassiferModel():
     cbc = CatBoostClassifier(iterations=30,learning_rate=0.2)
     return cbc
def run_model(model,x_train,y_train,x_test):
      model.fit(x_train,y_train)
      y_pred = model.predict(x_test)
      return y_pred