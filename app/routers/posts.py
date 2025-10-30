from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.schemas.post import PostBase, PostDisplay, UserPostDisplay
from app.database.session import get_db
from app.crud import post as crud_post

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.post("", response_model=UserPostDisplay, dependencies=[Depends(get_current_user)])
def create_post(post: PostBase, db: Session = Depends(get_db), current_user_id = Depends(get_current_user)):
    return crud_post.create_post(db, post, current_user_id)

@router.get("/all", response_model=list[UserPostDisplay], dependencies=[Depends(get_current_user)] )
def list_posts(db: Session = Depends(get_db), current_user_id = Depends(get_current_user)):
    return crud_post.get_all_posts_by_user(db, current_user_id)

@router.get("/all-posts", response_model=list[PostDisplay], dependencies=[Depends(get_current_user)] )
def list_posts(db: Session = Depends(get_db)):
    return crud_post.get_all_posts(db)
