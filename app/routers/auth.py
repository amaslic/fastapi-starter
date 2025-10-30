from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.user import UserBase, UserDisplay
from app.database.session import get_db
from app.crud import user as crud_user
from app.core.security import create_access_token
from app.utils.hashing import verify_password

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserDisplay)
def register_user(request: UserBase, db: Session = Depends(get_db)):
    existing = crud_user.get_user_by_email(db, request.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")
    new_user = crud_user.create_user(db, request.email, request.password)
    return new_user

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)): 
    user = crud_user.get_user_by_email(db, form_data.username) 
    if not user or not verify_password(form_data.password, user.password): 
        raise HTTPException(status_code=401, detail="Invalid credentials") 
    token = create_access_token({"sub": str(user.id)}) 
    return {"access_token": token, "token_type": "bearer"}

@router.post("/", response_model=UserDisplay)
def login(request: UserBase, db: Session = Depends(get_db)):
    user = crud_user.get_user_by_email(db, request.email)
    if not user or not verify_password(request.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}