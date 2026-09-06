"""EvaluationResult - stores the AI quality-control layer's output."""

from datetime import datetime, timezone

from sqlalchemy import JSON, DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class EvaluationResult(Base):
    __tablename__ = "evaluation_results"

    id: Mapped[int] = mapped_column(primary_key=True)

    artifact_type: Mapped[str] = mapped_column(String(50))
    artifact_id: Mapped[int] = mapped_column(Integer)

    quality_score: Mapped[float] = mapped_column(Float)
    checks: Mapped[dict] = mapped_column(JSON, default=dict)
    issues: Mapped[list] = mapped_column(JSON, default=list)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )
