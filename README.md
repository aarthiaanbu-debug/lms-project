# LMS Subscription Video Learning Platform

This project is a simple Learning Management System built using **Django Admin** and **FastAPI**.

The platform allows admins to manage courses and lessons, while users can subscribe to plans, enroll in courses, and track their learning progress.

---

## 🚀 Tech Stack

- Python
- Django (Admin Panel)
- FastAPI (API Development)
- SQLAlchemy
- Pydantic
- SQLite Database

---

## 📚 Features

- Course Management
- Lesson Management
- User Enrollment
- Subscription Plans
- Track Course Progress
- REST API using FastAPI

---

## 📂 Project Structure
lms-project/
│
├── learning/ # Django project
├── lms_admin/ # Django admin app
├── main.py # FastAPI application
├── models.py # SQLAlchemy models
├── schemas.py # Pydantic schemas
├── database.py # Database connection
├── manage.py # Django management
└── db.sqlite3 # SQLite database
⚙️ Setup Instructions

 1 Install Dependencies

pip install fastapi uvicorn sqlalchemy django pydantic

2 Run Django Server
python manage.py runserver
http://127.0.0.1:8000/admin
3 Run FastAPI Server
python-m uvicorn main:app --reload --port 8001
http://127.0.0.1:8001/docs

🔗 API Endpoints
| Method | Endpoint   | Description              |
| ------ | ---------- | ------------------------ |
| GET    | /courses   | Get all courses          |
| GET    | /lessons   | Get all lessons          |
| GET    | /plans     | Get subscription plans   |
| POST   | /subscribe | Subscribe to a plan      |
| POST   | /enroll    | Enroll in a course       |
| POST   | /progress  | Update learning progress |

