"""Target model.

Represents one entry in the fictional PR target dataset (Phase 6 populates
this table). Fields match PRD section 4 - deliberately generic across
categories rather than having category-specific columns.
"""

from sqlalchemy import JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Target(Base):
    __tablename__ = "targets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    category: Mapped[str] = mapped_column(String(100))
    organization: Mapped[str] = mapped_column(String(200))
    location: Mapped[str] = mapped_column(String(200))

    topics: Mapped[list] = mapped_column(JSON, default=list)
    industries: Mapped[list] = mapped_column(JSON, default=list)
    audience: Mapped[list] = mapped_column(JSON, default=list)
    preferred_themes: Mapped[list] = mapped_column(JSON, default=list)

    description: Mapped[str] = mapped_column(Text)

    example_email: Mapped[str | None] = mapped_column(String(200), nullable=True)

    campaign_targets: Mapped[list["CampaignTarget"]] = relationship(back_populates="target")
