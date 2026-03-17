from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base


class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True, index=True)
	username = Column(String(128), unique=True, index=True, nullable=False)
	email = Column(String(256), unique=False, index=True, nullable=True)
	hashed_password = Column(String(256), nullable=False)
	created_at = Column(DateTime(timezone=True), server_default=func.now())
