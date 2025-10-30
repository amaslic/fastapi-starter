from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from app.database.session import Base
import datetime
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    posts = relationship("DbPost", back_populates="creator")

class DbPost(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.now)
    creator_id = Column(Integer, ForeignKey("users.id"))  # FK ka users

    creator = relationship("DbUser", back_populates="posts")
