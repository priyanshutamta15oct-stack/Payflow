from fastapi import APIRouter
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



router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/signup")
def signup(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    created_user = create_user(
        db,
        user.full_name,
        user.email,
        user.password
    )

    if not created_user:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return {
        "message": "User Created Successfully"
    }


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

        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    return {
        "access_token": token,
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