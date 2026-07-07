from sklearn.metrics  import accuracy_score,classification_report,confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


def model_accuracy(y_true,y_pred):
    return accuracy_score(y_true,y_pred)

def model_confusion_matrix(y_true,y_pred):
    return sns.heatmap(confusion_matrix(y_true,y_pred),annot=False,cmap="coolwarm")
    
def model_classfication_report(y_true,y_pred):
    return classification_report(y_true,y_pred)