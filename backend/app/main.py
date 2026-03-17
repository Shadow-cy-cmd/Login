import os
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	# allow all origins for development. Narrow this in production.
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


class RegisterRequest(BaseModel):
	username: str
	password: str
	email: str | None = None


class LoginRequest(BaseModel):
	username: str
	password: str


def get_password_hash(password: str) -> str:
	return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
	return pwd_context.verify(plain_password, hashed_password)


@app.post('/register')
def register(req: RegisterRequest, db: Session = Depends(get_db)):
	existing = db.query(models.User).filter(models.User.username == req.username).first()
	if existing:
		raise HTTPException(status_code=400, detail='username already exists')

	user = models.User(
		username=req.username,
		email=req.email,
		hashed_password=get_password_hash(req.password),
	)
	db.add(user)
	db.commit()
	db.refresh(user)
	return {"message": f"registered {user.username}"}


@app.post('/login')
def login(req: LoginRequest, db: Session = Depends(get_db)):
	user = db.query(models.User).filter(models.User.username == req.username).first()
	if not user or not verify_password(req.password, user.hashed_password):
		raise HTTPException(status_code=401, detail='invalid credentials')
	return {"message": f"hi {user.username}"}
