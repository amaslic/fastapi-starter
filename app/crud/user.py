from sqlalchemy.orm import Session
from app.database.models import DbUser
from app.utils.hashing import hash_password

def get_user_by_email(db: Session, email: str):
    return db.query(DbUser).filter(DbUser.email == email).first()

def create_user(db: Session, email: str, password: str):
    new_user = DbUser(email=email, password=hash_password(password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
