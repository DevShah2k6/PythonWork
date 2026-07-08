from sklearn.metrics  import accuracy_score,classification_report,confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


def model_accuracy(y_true,y_pred):
    """
    Calculates the accuracy of model predictions.

    Args:
        y_true: Ground truth (actual) labels.
        y_pred: Predicted labels from the model.

    Returns:
        float: Accuracy score between 0 and 1.
    """
    return accuracy_score(y_true,y_pred)

def model_confusion_matrix(y_true,y_pred):
    '''
    Shows the confusion Matrix in which it shows True Positve and True Negative
    and False Positive and False Negative

    Args:
        y_true: Ground truth (actual) labels.
        y_pred: Predicted labels from the model.
    
    Returns:
        numpy.ndarray: The confusion matrix showing true positives,
        true negatives, false positives, and false negatives.
    '''
    return sns.heatmap(confusion_matrix(y_true,y_pred),annot=False,cmap="coolwarm")
    
def model_classification_report(y_true,y_pred):
    '''
    Shows the Classfication report in that F1-Score,Recall,Precision,Accuracy 
    it contains

    Args:
        y_true: Ground truth (actual) labels.
        y_pred: Predicted labels from the model.

    Returns:

    '''
    return classification_report(y_true,y_pred)