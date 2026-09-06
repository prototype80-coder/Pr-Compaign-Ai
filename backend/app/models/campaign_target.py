"""CampaignTarget - the relationship between a campaign and a target.

This is where MatchingService (Phase 9) stores the deterministic score and
its human-readable reasons, StoryAngleService (Phase 10) stores the
recommended angle, and outreach status (PRD section 8) is tracked.
"""

from sqlalchemy import JSON, Float, ForeignKey, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class CampaignTarget(Base):
    __tablename__ = "campaign_targets"
    __table_args__ = (UniqueConstraint("campaign_id", "target_id", name="uq_campaign_target"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    campaign_id: Mapped[int] = mapped_column(ForeignKey("campaigns.id"))
    target_id: Mapped[int] = mapped_column(ForeignKey("targets.id"))

    relevance_score: Mapped[float] = mapped_column(Float)
    matching_reasons: Mapped[list] = mapped_column(JSON, default=list)

    recommended_angle: Mapped[str | None] = mapped_column(Text, nullable=True)

    outreach_status: Mapped[str] = mapped_column(String(50), default="not_contacted")

    campaign: Mapped["Campaign"] = relationship(back_populates="campaign_targets")
    target: Mapped["Target"] = relationship(back_populates="campaign_targets")
    outreach_drafts: Mapped[list["OutreachDraft"]] = relationship(
        back_populates="campaign_target", cascade="all, delete-orphan"
    )
