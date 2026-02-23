# FastAPI Blog Application

A professional and robust blog API built with **FastAPI**, **SQLAlchemy**, and **JWT Authentication**. This project allows users to create, read, update, and delete blog posts while ensuring secure access through user authentication.

## 🚀 Features

- **User Management**:
  - User registration and password hashing.
  - User retrieval by ID.
- **Blog Management**:
  - Create blog posts (authenticated).
  - List all blog posts.
  - Get a specific blog post with creator information.
  - Update and Delete blog posts (only by the creator).
- **Security**:
  - JWT (JSON Web Token) authentication.
  - Password hashing using `Argon2` (via `passlib`).
  - Route protection (creator-only access for sensitive actions).

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: SQLite (SQLAlchemy ORM)
- **Authentication**: JWT (OAuth2 with Password Flow)
- **Validation**: Pydantic
- **Packaging**: `uv` or `pip`

## 📁 Project Structure

```text
e:/Blog
├── routeres/           # API Endpoints (Blog, User, Auth)
├── repositry/          # Business logic & DB operations
├── models.py           # SQLAlchemy Database Models
├── schemas.py          # Pydantic Schemas for validation
├── db.py               # Database connection setup
├── hashing.py          # Password hashing utilities
├── tokens.py           # JWT token generation & verification
├── aouth2.py           # OAuth2 authentication logic
├── main.py             # Entry point of the application
└── requirements.txt    # Project dependencies
```

## ⚙️ Installation & Usage

### 1. Clone the repository
```bash
git clone <repository-url>
cd Blog
```

### 2. Set up Virtual Environment
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
uvicorn main:app --reload
```

## 📖 API Documentation

Once the server is running, you can access the interactive documentation:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 👤 Author

**Muhammad Altaf**
- [GitHub](https://github.com/altaf59)
- [Portfolio](https://altaf59.github.io)
