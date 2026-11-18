# 🌾 Crop Price Prediction

A Machine Learning-based web application that predicts crop prices based on agricultural and environmental parameters.

## 📌 Project Overview

Crop Price Prediction helps estimate crop prices using Machine Learning techniques. The application allows users to enter relevant agricultural parameters and get predicted crop prices through an interactive web interface.

## ✨ Features

- Predict crop prices using Machine Learning.
- User-friendly React.js interface.
- FastAPI-based backend.
- Trained Machine Learning model for predictions.
- Data preprocessing and feature engineering.
- Model performance evaluation.
- REST API integration.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Frontend | React.js |
| Backend | Python, FastAPI |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas |
| Model Serialization | Joblib |

## 📂 Project Structure

```text
Crop-Price-Prediction/
│
├── backend/
│   ├── ML/
│   │   ├── models/
│   │   ├── dataset/
│   │   ├── prediction.py
│   │   └── train_test_spliting.py
│   ├── models/
│   ├── routes/
│   ├── database.py
│   └── main.py
│
├── frontend/
│   └── Crop-price-Prediction/
│       ├── src/
│       ├── public/
│       ├── package.json
│       └── vite.config.js
│
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone -b Crop-Price-Prediction-Project https://github.com/DevShah2k6/PythonWork.git
```

### 2. Navigate to the Project

```bash
cd PythonWork
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Backend

```bash
cd backend
uvicorn main:app --reload
```

### 7. Run the Frontend

Open another terminal:

```bash
cd frontend/Crop-price-Prediction
npm install
npm run dev
```

## 🚀 How It Works

1. User enters agricultural and environmental parameters.
2. Frontend sends the input data to the FastAPI backend.
3. Backend preprocesses the input data.
4. Trained Machine Learning model predicts the crop price.
5. Predicted price is displayed on the frontend.

## 🎯 Project Objective

The objective is to support agricultural price estimation through Machine Learning and provide users with an accessible platform for predicting crop prices.

## 👨‍💻 Author

**Dev Shah**

GitHub: [DevShah2k6]

---

⭐ If you find this project useful, consider giving it a star!
