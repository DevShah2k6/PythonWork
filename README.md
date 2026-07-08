# BBC News Text Classification using Machine Learning

## Project Overview

This project classifies BBC news articles into different categories using Natural Language Processing (NLP) and Machine Learning.

The text is preprocessed, converted into numerical features using TF-IDF, and then multiple machine learning models are trained and evaluated.

---

## Features

- Data preprocessing
- Text cleaning
- Category encoding
- TF-IDF Vectorization
- Multiple Machine Learning models
- Model evaluation
- Predict category for custom user input

---
## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn (Machine Learning Models)
- SpaCy (Text Preprocessing)
- XGBoost
- Matplotlib (Data Visualization)
- Seaborn (Data Visualization)


---

## Dataset

This project uses the **BBC News Dataset**, which contains news articles labeled with their respective categories (e.g., business, sports, politics, tech, entertainment).

- **Source:** [BBC News Dataset on Kaggle](https://www.kaggle.com/datasets/shineucc/bbc-news-dataset)
- **File required:** `BBC news dataset.csv`

### Setup Instructions
1. Download the dataset from the link above.
2. Place the file (`BBC news dataset.csv`) in the project's root directory.
3. Ensure the filename matches exactly, as the code reads it directly using this name.

---

## Machine Learning Models(Used)

- Logistic Regression
- Multinomial Naive Bayes
- K-Nearest Neighbors
- Decision Tree
- Random Forest
- SVC 
- Linear SVC 
- XGBoost
- CatBoost

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory

```bash
cd <repository-folder>
```

Install the required libraries

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python main.py
```

---

## Project Structure

```text
project/
│
├── __pycache__/
├── catboost_info/
├── .gitignore
├── BBC news dataset.csv
├── encoded.py
├── evaluation.py
├── featureengineering.py
├── main.py
├── models.py
├── prediction.py
├── preprocessingdataframe.py
├── preprocessingtext.py
├── README.md
├── requirements.txt
├── traintestsplit.py
├── treeplotandfeatureimportance.py
└── vectorizer.pkl
```

## Future Improvements

- Hyperparameter tuning
- Deep Learning models
- Streamlit web application
- Model deployment using FastAPI

---

## Author

Dev Shah