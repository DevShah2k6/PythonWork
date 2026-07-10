from sklearn.model_selection import train_test_split
def train_test_split_data(x,y):
    """
    Splits the dataset into training and testing data.

    The training data is used to train the model, while the testing
    data is used to evaluate model performance.
    """
    return train_test_split(x,y,test_size=0.3,random_state=42,stratify=y)