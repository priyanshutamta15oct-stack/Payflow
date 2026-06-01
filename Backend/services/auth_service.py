from sqlalchemy.orm import Session
from models.user_model import User

from core.logger import logger

from core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token
)


def create_user(
        db: Session,
        full_name: str,
        email: str,
        password: str
):

    logger.info(f"Signup attempt for email: {email}")

    existing_user = db.query(User).filter(
        User.email == email
    ).first()

    if existing_user:

        logger.warning(
            f"Duplicate signup attempt: {email}"
        )

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

    logger.info(
        f"User created successfully: {new_user.email}"
    )

    return new_user


def login_user(
        db: Session,
        email: str,
        password: str
):

    logger.info(
        f"Login attempt for email: {email}"
    )

    user = db.query(User).filter(
        User.email == email
    ).first()

    # USER NOT FOUND
    if not user:

        logger.warning(
            f"Login failed - user not found: {email}"
        )

        return None

    # PASSWORD CHECK
    if not verify_password(
        password,
        user.hashed_password
    ):

        logger.warning(
            f"Login failed - invalid password: {email}"
        )

        return None

    # ACCESS TOKEN
    access_token = create_access_token(
        {"sub": user.email}
    )

    # REFRESH TOKEN
    refresh_token = create_refresh_token(
        {"sub": user.email}
    )

    logger.info(
        f"User logged in successfully: {email}"
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }