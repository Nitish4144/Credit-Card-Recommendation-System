from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.logger import logger


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception
    ):

        logger.exception(
            "Unhandled exception occurred"
        )

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": str(exc)
            }
        )