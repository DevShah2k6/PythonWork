from sklearn.model_selection import train_test_split
def train_test_split_data(x,y):
    return train_test_split(x,y,test_size=0.3,random_state=42)