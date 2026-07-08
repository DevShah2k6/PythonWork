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
from evaluation import model_classfication_report,model_accuracy,model_confusion_matrix
#here it follows the o->open for extensiona dn closed for chnaging the code 
#foloows the solid principle

def build_logitstic_regression_model():
    '''"""
    Trains a Logistic Regression classification model.
     It learns patterns from training data and predicts categories
    based on the learned decision boundaries
    '''
    loreg = LogisticRegression(max_iter=300,random_state=42)
    return loreg
def build_decisiontree_classifier_model():
     """
    Trains a Decision Tree classification model.

    The model learns decision rules from features to classify data
    into different categories.
    """
     dtc = DecisionTreeClassifier(max_depth=22,random_state=42,min_samples_leaf=4)
     return dtc
def build_random_forest_classifier_model():
     """
    Trains a Random Forest classification model.

    It combines multiple decision trees to improve prediction accuracy
    and reduce overfitting.
    """
     rfc = RandomForestClassifier(n_estimators=1000,max_depth=25,random_state=42)
     return rfc

def build_svc_model():
     """
    Trains a Support Vector Classification model.

    It finds the best separating boundary between different classes
    for text classification.
    """
     svc  = SVC(C=0.3,random_state=42)
     return svc
def build_multinomial_nb_model():
     """
    Trains a Multinomial Naive Bayes model.

    It is commonly used for text classification problems and predicts
    categories based on word probabilities.
    """
     mnb = MultinomialNB()
     return mnb
def build_k_neighbors_classifier_model():
     """
    Trains a K-Nearest Neighbors classification model.

    It predicts classes by comparing new data with similar examples
    from the training dataset.
    """
     knn = KNeighborsClassifier(n_neighbors=5)
     return knn
def build_xgb_classifier_model():
    """
    Creates and returns an XGBoost classification model.

    It uses multiple boosting trees to improve classification performance.
    """
    xgb = XGBClassifier(
        objective="multi:softmax",
        eval_metric="mlogloss",
        random_state=42
    )
    return xgb


def build_linear_svc_model():
     """
    Trains a Linear Support Vector Classification model.

    It finds the best separating boundary between different classes
    for text classification.
    """
     lsvc = LinearSVC(C=0.2,random_state=42,max_iter=2000)
     return lsvc

def build_catboost_classifier_model():
     '''
     Trains a CatBoost classification model using the training data.

    CatBoostClassifier is a gradient boosting algorithm used for
    classification tasks. It builds multiple decision trees sequentially
    to improve prediction performance.

    Args:
        x_train: Training feature data used for model training.
        y_train: Training target labels used for learning classes.

    Returns:
        Trained CatBoostClassifier model.
    '''
     cbc = CatBoostClassifier(iterations=30,learning_rate=0.2)
     return cbc
def run_model(model,x_train,y_train,x_test):
     """
     Trains the given model on training data and returns predictions
     for the test data.
     """
     model.fit(x_train,y_train)
     y_pred = model.predict(x_test)
     return y_pred