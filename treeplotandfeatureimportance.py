from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
def plotting_tree(model):
    plot_tree(model)
    plt.show()

def feature_importance_dtc(model,vectorizer):
    plt.figure(figsize=(12,14))
    plt.bar(vectorizer.get_feature_names_out(),model.feature_importances_)
    plt.title("Feature Importances of Decision Tree Classifer")
    plt.xticks(rotation=45)
    plt.show()

def feature_importance_rfc(model,vectorizer):
    plt.figure(figsize=(12,14))
    plt.bar(vectorizer.get_feature_names_out(),model.feature_importances_)
    plt.title("Feature Importances of Random Tree Classifer")
    plt.xticks(rotation=45)
    plt.show()