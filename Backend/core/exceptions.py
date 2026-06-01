from fastapi import Request
from fastapi.responses import JSONResponse

from core.logger import logger


class AppException(Exception):

    def __init__(
        self,
        status_code: int,
        detail: str
    ):
        self.status_code = status_code
        self.detail = detail


async def app_exception_handler(
    request: Request,
    exc: AppException
):

    logger.warning(
        f"Application exception: {exc.detail}"
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.detail
        }
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception
):

    logger.error(
        f"Unexpected server error: {str(exc)}"
    )

    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error"
        }
    )