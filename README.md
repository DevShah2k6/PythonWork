# 🎓 Student Application using PyMongo

A full-stack Student Management Application built using **FastAPI, MongoDB (PyMongo), and React**. This application allows users to manage student records through a user-friendly interface with CRUD (Create, Read, Update, Delete) operations.

## 🚀 Features

- Add new students
- View all registered students
- Edit student details
- Delete student records
- Form validation
- FastAPI REST API integration
- MongoDB database integration using PyMongo
- React frontend with React Router

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| **Backend** | Python, FastAPI, PyMongo, Pydantic, MongoDB, Uvicorn |
| **Frontend** | React, Vite, React Router, JavaScript, CSS, Fetch API |

## 📂 Project Structure

```text
Student-Application-using-PyMongo/
│
├── backend/
│   ├── database.py
│   ├── main.py
│   ├── models/
│   │   └── model.py
│   └── routes/
│       └── route.py
│
├── frontend/
│   └── Student-Form-Details/
│       ├── public/
│       ├── src/
│       │   ├── api/
│       │   │   └── api.js
│       │   ├── assets/
│       │   │   └── style/
│       │   ├── components/
│       │   │   ├── EditForm.jsx
│       │   │   ├── Home.jsx
│       │   │   ├── Navbar.jsx
│       │   │   ├── StudentForm.jsx
│       │   │   └── StudentList.jsx
│       │   ├── App.jsx
│       │   ├── App.css
│       │   ├── index.css
│       │   └── main.jsx
│       ├── index.html
│       ├── package.json
│       └── vite.config.js
│
└── .gitignore
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

Navigate to the project directory:

```bash
cd Student-Application-using-PyMongo
```

### 2. Backend Setup

Navigate to the backend folder:

```bash
cd backend
```

Create a virtual environment:

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install backend dependencies:

```bash
pip install fastapi uvicorn pymongo pydantic
```

### 3. MongoDB Configuration

Make sure MongoDB is running and configure your MongoDB connection string in `database.py`.

Example:

```python
MONGO_URI = "mongodb://localhost:27017/"
```

Update the connection string according to your MongoDB configuration.

### 4. Run the Backend

From the `backend` folder, run:

```bash
uvicorn main:app --reload
```

Backend API:

`http://127.0.0.1:8000`

FastAPI Swagger Documentation:

`http://127.0.0.1:8000/docs`

### 5. Frontend Setup

Open another terminal and navigate to the frontend folder:

```bash
cd frontend/Student-Form-Details
```

Install dependencies:

```bash
npm install
```

Run the React development server:

```bash
npm run dev
```

Frontend application:

`http://localhost:5173`

## 🔄 Application Workflow

```text
       React Frontend
              |
              ↓
       Fetch API Requests
              |
              ↓
        FastAPI Backend
              |
              ↓
          API Routes
              |
              ↓
       Pydantic Models
              |
              ↓
         PyMongo Driver
              |
              ↓
           MongoDB
```

## 📌 CRUD Operations

| Operation | Description |
|---|---|
| Create | Add a new student record |
| Read | Display all registered students |
| Update | Edit existing student details |
| Delete | Remove student records |

## 🔐 Environment & Security

- Keep database credentials and sensitive configuration in environment variables.
- Do not upload `.env` files to GitHub.
- Keep `node_modules`, virtual environments, and Python cache files out of version control.

## 👨‍💻 Author

**Dev Shah**
