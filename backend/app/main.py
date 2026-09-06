"""FastAPI application entrypoint.

Assembles the app, registers routers, and installs a global exception
handler so AppError subclasses (raised anywhere in services/) become
consistent, user-safe JSON responses instead of unhandled 500s with stack
traces.
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api import health
from app.core.errors import AIProviderError, AppError, NotFoundError, ValidationFailedError

app = FastAPI(
    title="PR Campaign Copilot API",
    description="Explainable PR targeting and outreach strategy backend.",
    version="0.1.0",
)

app.include_router(health.router)


@app.exception_handler(AppError)
def handle_app_error(request: Request, exc: AppError) -> JSONResponse:
    status_code = 500
    if isinstance(exc, NotFoundError):
        status_code = 404
    elif isinstance(exc, ValidationFailedError):
        status_code = 422
    elif isinstance(exc, AIProviderError):
        status_code = 502

    return JSONResponse(
        status_code=status_code,
        content={"error": exc.message},
    )
