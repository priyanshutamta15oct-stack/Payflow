from fastapi import APIRouter, logger
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database.session import get_db

from schemas.user_schema import (
    UserCreate,
    UserLogin,
    TokenResponse
)

from services.auth_service import (
    create_user,
    login_user
)

from core.dependencies import get_current_user
from models.user_model import User
from fastapi.security import OAuth2PasswordRequestForm
from database.redis_db import redis_client
from core.dependencies import oauth2_scheme
from jose import jwt
from jose import JWTError

from core.security import create_access_token
from core.config import settings
from core.logger import logger


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/signup")
def signup(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    try:

        created_user = create_user(
            db,
            user.full_name,
            user.email,
            user.password
        )

        return {
            "message": "User Created Successfully"
        }

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    token = login_user(
        db,
        form_data.username,
        form_data.password
    )

    if not token:

        logger.warning(
            f"Authentication failed for: {form_data.username}"
        )

        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    logger.info(
        f"Authentication successful for: {form_data.username}"
    )

    return {
        "access_token": token["access_token"],
        "refresh_token": token["refresh_token"],
        "token_type": "bearer"
    }

@router.get("/profile")
def get_profile(
    current_user: User = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "full_name": current_user.full_name,
        "email": current_user.email
    }

@router.post("/logout")
def logout(token: str = Depends(oauth2_scheme)):
    redis_client.set(token, "blacklisted", ex=1800)  # Blacklist token for 1 hour
    return {
        "message": "Logged out successfully"
    }

@router.post("/refresh")
def refresh_token(refresh_token: str):

    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid refresh token"
    )

    try:

        payload = jwt.decode(
            refresh_token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise credentials_exception

        new_access_token = create_access_token(
            {"sub": email}
        )

        return {
            "access_token": new_access_token,
            "token_type": "bearer"
        }

    except JWTError:
        raise credentials_exception