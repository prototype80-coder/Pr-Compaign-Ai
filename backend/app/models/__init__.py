"""Import every model here so create_all() and relationship() string
references can find every table."""

from app.models.campaign import Campaign
from app.models.campaign_target import CampaignTarget
from app.models.evaluation_result import EvaluationResult
from app.models.outreach_draft import OutreachDraft
from app.models.target import Target

__all__ = [
    "Campaign",
    "Target",
    "CampaignTarget",
    "OutreachDraft",
    "EvaluationResult",
]
