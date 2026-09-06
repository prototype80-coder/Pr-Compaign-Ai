"""Health check endpoint.

Used for uptime checks / confirming the API is running and configured.
Deliberately has no dependencies on the database or AI provider - it should
succeed even if those are down, since its only job is confirming the API
process itself is alive.
"""

from fastapi import APIRouter

from app.core.config import get_settings

router = APIRouter()


@router.get("/health")
def health_check() -> dict:
    settings = get_settings()
    return {
        "status": "healthy",
        "environment": settings.environment,
    }
