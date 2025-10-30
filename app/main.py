from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.session import Base, engine
from app.routers import auth, posts
from fastapi.openapi.utils import get_openapi

# Kreiraj tabele
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Starter")

# Mount routers
app.include_router(auth.router)
app.include_router(posts.router)

# CORS middleware
origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


