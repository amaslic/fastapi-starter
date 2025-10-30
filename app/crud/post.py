from sqlalchemy.orm import Session
from app.database.models import DbPost
import datetime

def create_post(db: Session, post_data, creator_id: int):
    new_post = DbPost(
        title=post_data.title,
        content=post_data.content,
        creator_id=creator_id,
        timestamp=datetime.now(datetime.timezone.utc)
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all_posts(db: Session):
    return db.query(DbPost).all()

def get_all_posts_by_user(db: Session, creator_id: int):
    return db.query(DbPost).filter(DbPost.creator_id == creator_id).all()

def get_post_by_id(db: Session, id: int):
    return db.query(DbPost).filter(DbPost.id == id).first()

def delete_post_by_id(db: Session, id: int):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if post:
        db.delete(post)
        db.commit()
        return True
    return False
