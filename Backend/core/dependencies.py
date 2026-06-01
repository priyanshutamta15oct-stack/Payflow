from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError
from jose import jwt

from sqlalchemy.orm import Session

from database.session import get_db
from database.redis_db import redis_client

from models.user_model import User

from core.config import settings
from core.logger import logger


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:

    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # CHECK REDIS BLACKLIST FIRST
    if redis_client.get(token):

        logger.warning(
            "Blacklisted token access attempt detected"
        )

        raise HTTPException(
            status_code=401,
            detail="You have been logged out"
        )

    try:

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        email: str = payload.get("sub")

        if email is None:

            logger.warning(
                "JWT token missing subject field"
            )

            raise credentials_exception

    except JWTError:

        logger.warning(
            "Invalid or expired JWT token received"
        )

        raise credentials_exception

    user = db.query(User).filter(
        User.email == email
    ).first()

    if user is None:

        logger.warning(
            f"Token valid but user not found: {email}"
        )

        raise credentials_exception

    logger.info(
        f"Authenticated user: {user.email}"
    )

    return user