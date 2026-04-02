# FastAPI User Registration API

This project is a backend application built using **FastAPI** that implements a **User Registration System** using RESTful APIs. It allows users to register, store their data in a database, and manage user records with proper backend structure.
---

## 🚀 Overview
This project focuses on building a basic authentication-related system where users can:
* Register with required details (username, email, password)
* Store user data securely in a database
* Retrieve user information
* Update or delete user records
It demonstrates how real-world applications handle user data instead of just temporary storage.
---

## ⚙️ Features
* User registration with validation
* Store user data in database (SQLite / other DB)
* Retrieve all users or specific user by ID
* Update user details
* Delete user accounts
* RESTful API design
* Automatic API documentation (`/docs`)
* Clean and modular architecture
---

## 🛠️ Tech Stack
* **Backend**: FastAPI
* **Language**: Python
* **Database**: SQLite
* **Frontend**: Html,Css,Javascript
* **Validation**: Pydantic
* **Server**: Uvicorn

---

## 📂 Project Structure

```id="1vbn0d"
project/
│── main.py              # Entry point
│── database.py          # DB connection
│── models.py            # User table (SQLAlchemy)
│── schemas.py           # Request/response models
│── crud.py              # Database operations
│── routers/             # API routes
│── requirements.txt     # Dependencies
```

---


## ▶️ How to Run
1. Run the server:

   ```
   uvicorn main:app --reload
   ```
2. Open API docs:

   ```
   http://127.0.0.1:8000/docs
   ```

## 🧠 What This Project Teaches

Most beginners build registration systems incorrectly by:
* Storing plain-text passwords
* Mixing database logic inside routes
* Skipping validation
This project helps you understand:
* Proper data validation using Pydantic
* Database handling using SQLAlchemy
* Clean separation between routes, logic, and models
* Basic structure of authentication systems

## 📎 Conclusion
This project demonstrates how to build a basic user registration backend using FastAPI. It provides a strong foundation for understanding how user data is handled in real-world applications and prepares you for building secure authentication systems.
