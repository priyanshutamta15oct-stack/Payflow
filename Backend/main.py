from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.test import router as test_router
from routers.auth_router import router as auth_router
from models.user_model import User
from database.db import Base, engine
from models.payment_model import Payment


Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(test_router)
app.include_router(auth_router)
Base.metadata.create_all(bind=engine)
from routers.payment_router import (router as payment_router)
app.include_router(payment_router)

app.add_middleware(
    CORSMiddleware,     
    allow_origins=["http://localhost:5173"],  # Allow all origins (you can specify specific origins if needed)
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
    allow_credentials=True,  # Allow cookies and credentials
)   

@app.get("/")

def home():
    return {
        "message": "Welcome to the Payflow API!"
    }