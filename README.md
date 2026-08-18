# PaddleOCR Receipt Project

A simple receipt OCR project that uses **PaddleOCR** to extract information from receipt PDFs and save the required receipt details in a database.

## Features

* Upload a receipt PDF.
* Extract text from the receipt using PaddleOCR.
* Automatically read important receipt details.
* Show the extracted details in a form.
* Allow the user to edit the details.
* Save the final receipt details in SQLite database.
* View saved receipts from the frontend.

## Project Structure

```text
PaddleOCR-Project/
│
├── backend/
│   ├── upload/
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── ocr.py
│   ├── requirements.txt
│   └── schemas.py
│
├── frontend/
│
├── .gitignore
└── README.md
```

## Technologies Used

### Backend

* Python
* FastAPI
* PaddleOCR
* SQLite
* SQLAlchemy

### Frontend

* React
* Vite
* JavaScript

## How It Works

1. User uploads a receipt PDF.
2. Backend receives the PDF.
3. PaddleOCR extracts the text from the receipt.
4. Required receipt fields are parsed from the OCR result.
5. The fields are shown in the frontend form.
6. User can edit the fields if required.
7. User clicks **Submit**.
8. Receipt details are saved in the SQLite database.
9. Saved receipts can be viewed from the Receipts page.

## Receipt Fields

The project stores fields such as:

* Store Name
* Invoice Number
* Date
* Customer Name
* Phone Number
* Payment Mode
* Subtotal
* CGST
* SGST
* Total Amount

## Backend Setup

Go to the backend folder:

```bash
cd backend
```

Create and activate a Python virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The backend will run on:

```text
http://127.0.0.1:8000
```

## Frontend Setup

Go to the frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the frontend:

```bash
npm run dev
```

The frontend will run on the URL shown by Vite in the terminal.

## Database

The project uses **SQLite** to store the final receipt fields after the user submits the receipt form.

## Note

The `backend/upload` folder is used for uploaded receipt files and is ignored by Git using `.gitignore`.
