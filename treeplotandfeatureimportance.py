from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
def plotting_tree(model):
    """
    Displays the structure of a trained decision tree model.

    It shows how the tree makes decisions using different features.
    """
    plot_tree(model)
    plt.show()

def feature_importance_dtc(model,vectorizer):
    """
    Calculates and displays important features used by the model.

    It shows which words/features have more influence on predictions.
    """
    plt.figure(figsize=(12,14))
    plt.bar(vectorizer.get_feature_names_out(),model.feature_importances_)
    plt.title("Feature Importances of Decision Tree Classifer")
    plt.xticks(rotation=45)
    plt.show()

def feature_importance_rfc(model,vectorizer):
    """
    Calculates and displays important features used by the model.

    It shows which words/features have more influence on predictions.
    """
    plt.figure(figsize=(12,14))
    plt.bar(vectorizer.get_feature_names_out(),model.feature_importances_)
    plt.title("Feature Importances of Random Tree Classifer")
    plt.xticks(rotation=45)
    plt.show()