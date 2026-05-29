from sqlalchemy.orm import Session
from models.user_model import User

from core.security import (
    hash_password,
    verify_password,
    create_access_token
)

def create_user(
        db: Session,
        full_name: str,
        email: str,
        password: str
):
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise ValueError("Email already registered")

    hashed_password = hash_password(password)
    new_user = User(
        full_name=full_name,
        email=email,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login_user(
        db: Session,
        email: str,
        password: str
):

    user = db.query(User).filter(
        User.email == email
    ).first()

    # USER NOT FOUND
    if not user:
        return None

    # PASSWORD CHECK
    if not verify_password(
        password,
        user.hashed_password
    ):
        return None

    # CREATE TOKEN
    token = create_access_token(
        {"sub": user.email}
    )

    return token