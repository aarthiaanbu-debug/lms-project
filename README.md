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

 1. Notifications System

A notification system was implemented to track important user activities.

Examples:

* User enrolled in a course
* Lesson completed
* New course updates

Notifications are stored in the database and displayed in the **Admin Dashboard**.

### 2. Admin Dashboard Analytics

The dashboard displays basic platform analytics such as:

* Total Users
* Total Courses
* Total Enrollments
* Completed Lessons
* Recent Notifications

This helps admins quickly monitor platform activity.

### 3. FastAPI Integration

FastAPI was used to expose simple API endpoints for the LMS system.

The API server can be started using:

```
[uvicorn main:app --reload](http://127.0.0.1:8001/docs)
```

### 4. API Testing with Postman

All API endpoints were tested using **Postman**.

Example endpoints tested:

* GET /courses
* GET /dashboard
* POST /enroll
* GET /notifications
