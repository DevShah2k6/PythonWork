from sklearn.metrics  import accuracy_score,classification_report,confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


def model_accuracy(y_true,y_pred):
    '''
    Caculates the Accuracy by taking the true data and predicted data
    '''
    return accuracy_score(y_true,y_pred)

def model_confusion_matrix(y_true,y_pred):
    '''
    Shows the confusion Matrix in which it shows True Positve and True Negative
    and Falso Positive and False Negative
    '''
    return sns.heatmap(confusion_matrix(y_true,y_pred),annot=False,cmap="coolwarm")
    
def model_classfication_report(y_true,y_pred):
    '''
    Shows the Classfication report in that F1-Score,Recall,Precision,Accuracy 
    it contains
    '''
    return classification_report(y_true,y_pred)