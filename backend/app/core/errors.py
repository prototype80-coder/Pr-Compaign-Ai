"""Shared error-handling foundation.

Every service-layer failure should raise one of these instead of a bare
Exception, so route handlers (and later, a global exception handler) can
map failures to consistent, user-safe API responses instead of leaking
stack traces.
"""


class AppError(Exception):
    """Base class for all application-raised errors."""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class AIProviderError(AppError):
    """Raised when the AI provider fails, times out, or returns something
    that doesn't parse into the expected schema."""


class ValidationFailedError(AppError):
    """Raised when input or AI output fails validation against a schema."""


class NotFoundError(AppError):
    """Raised when a requested resource (campaign, target, etc.) doesn't exist."""
