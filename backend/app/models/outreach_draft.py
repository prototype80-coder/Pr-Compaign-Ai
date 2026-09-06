"""OutreachDraft - a generated (and possibly user-edited) outreach message."""

from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class OutreachDraft(Base):
    __tablename__ = "outreach_drafts"

    id: Mapped[int] = mapped_column(primary_key=True)
    campaign_target_id: Mapped[int] = mapped_column(ForeignKey("campaign_targets.id"))

    subject: Mapped[str] = mapped_column(String(300))
    message: Mapped[str] = mapped_column(Text)
    personalization_rationale: Mapped[str] = mapped_column(Text)

    status: Mapped[str] = mapped_column(String(50), default="draft")

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )
    edited_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    campaign_target: Mapped["CampaignTarget"] = relationship(back_populates="outreach_drafts")
