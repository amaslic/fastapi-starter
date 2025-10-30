# 🚀 FastAPI Blog API

A modular **FastAPI** project featuring JWT authentication, SQLAlchemy ORM, and full Docker support for both development and production environments.  
It allows user registration, login, and creating posts associated with users.

---

## ✨ Features

- ✅ JWT-based authentication (secure login and protected routes)
- 🧑‍💻 CRUD operations for users and posts
- 🗄️ SQLAlchemy ORM integration
- 🧱 Modern, modular FastAPI project structure
- 🐳 Dockerized for both dev and prod environments
- 🔐 Password hashing with **bcrypt**
- 🌍 CORS middleware enabled for frontend integration

---

## 🧩 Tech Stack

- **FastAPI**
- **Python 3.11**
- **SQLAlchemy**
- **PostgreSQL**
- **Docker & Docker Compose**
- **bcrypt**
- **python-jose**
- **pydantic**

---

## ⚙️ Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/fastapi-blog-api.git
cd fastapi-blog-api
```

### 2. Build and start containers
```bash
docker compose build --no-cache
docker compose up api
```

The API will be available at:  
👉 `http://localhost:8000`

---

## 📂 Project Structure

```
app/
├── core/
│   ├── config.py          # Global settings (env variables, JWT secret, etc.)
│   ├── security.py        # JWT helpers and current_user dependency
├── crud/
│   ├── user.py            # User CRUD logic
│   ├── post.py            # Post CRUD logic
├── database/
│   ├── session.py         # SQLAlchemy DB session
│   ├── models.py          # Database models
├── routers/
│   ├── auth.py            # Auth routes (register/login)
│   ├── posts.py           # Post routes (create/get)
├── schemas/
│   ├── user.py            # Pydantic schemas for users
│   ├── post.py            # Pydantic schemas for posts
├── utils/
│   ├── hashing.py         # bcrypt password hashing utilities
└── main.py                # Application entry point
```

---

## 🔑 Authentication (JWT)

Authentication is handled with **JSON Web Tokens (JWT)**.  
A user logs in via `/auth/login` and receives an `access_token`.  
That token must be included in every protected route request:

```
Authorization: Bearer <your_token_here>
```

---

## 🧠 API Endpoints

### 👤 Auth
| Method | Endpoint         | Description |
|--------|------------------|--------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login`    | Log in and get JWT token |

### 📝 Posts
| Method | Endpoint         | Description |
|--------|------------------|--------------|
| POST | `/posts`         | Create a new post (requires JWT) |
| GET  | `/posts/all`     | Get all posts for user (requires JWT) |
| GET  | `/posts/all-posts`     | Get all posts (requires JWT) |

---

## ⚙️ Environment Variables

Edit an `.env` file in the root directory with the following values:

```
DATABASE_URL=postgresql://user:password@db:5432/blogdb || sqlite:///./app.db (recommended for local development)
JWT_SECRET=your_super_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=120
```

---

## 🧠 Development Notes

- API docs are available at:
  - Swagger UI → [http://localhost:8000/docs](http://localhost:8000/docs)
  - ReDoc → [http://localhost:8000/redoc](http://localhost:8000/redoc)
- Use **Postman** or **curl** for testing authenticated routes.
- In development, you can connect directly to the local SQLite or PostgreSQL database (depending on environment).

---

## 🧹 .gitignore

This project ignores all databases and Python cache folders:

```
*.db
__pycache__/
*/__pycache__/
```

---

## 🪪 License

This project is open-source under the **MIT License**.  
You’re free to use, modify, and distribute it.




