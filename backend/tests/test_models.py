from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.core.database import Base
from app.models import Campaign, CampaignTarget, EvaluationResult, OutreachDraft, Target


def make_test_session() -> Session:
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)
    return Session(engine)


def test_create_campaign():
    db = make_test_session()
    campaign = Campaign(name="AI Healthcare Launch", brief="Launching an AI healthcare startup.")
    db.add(campaign)
    db.commit()

    assert campaign.id is not None
    assert campaign.status == "draft"
    assert campaign.analysis is None


def test_create_target():
    db = make_test_session()
    target = Target(
        name="Jordan Rivera",
        category="journalist",
        organization="Gulf Tech Weekly",
        location="Dubai, UAE",
        topics=["AI", "healthcare"],
        industries=["technology", "healthcare"],
        audience=["business leaders"],
        preferred_themes=["innovation"],
        description="Covers enterprise tech across the UAE.",
    )
    db.add(target)
    db.commit()

    assert target.id is not None
    assert target.topics == ["AI", "healthcare"]


def test_campaign_target_relationship_and_score():
    db = make_test_session()
    campaign = Campaign(name="Launch", brief="brief text")
    target = Target(
        name="Jordan Rivera",
        category="journalist",
        organization="Gulf Tech Weekly",
        location="Dubai, UAE",
        topics=["AI"],
        industries=["technology"],
        audience=["business leaders"],
        preferred_themes=["innovation"],
        description="desc",
    )
    db.add_all([campaign, target])
    db.commit()

    link = CampaignTarget(
        campaign_id=campaign.id,
        target_id=target.id,
        relevance_score=87.0,
        matching_reasons=["Strong AI relevance", "UAE geographic relevance"],
    )
    db.add(link)
    db.commit()

    assert link.outreach_status == "not_contacted"
    assert campaign.campaign_targets[0].relevance_score == 87.0
    assert target.campaign_targets[0].campaign_id == campaign.id


def test_outreach_draft_and_evaluation_result():
    db = make_test_session()
    campaign = Campaign(name="Launch", brief="brief text")
    target = Target(
        name="Jordan Rivera",
        category="journalist",
        organization="Gulf Tech Weekly",
        location="Dubai, UAE",
        topics=["AI"],
        industries=["technology"],
        audience=["business leaders"],
        preferred_themes=["innovation"],
        description="desc",
    )
    db.add_all([campaign, target])
    db.commit()

    link = CampaignTarget(
        campaign_id=campaign.id, target_id=target.id, relevance_score=90.0, matching_reasons=[]
    )
    db.add(link)
    db.commit()

    draft = OutreachDraft(
        campaign_target_id=link.id,
        subject="Story idea: AI in UAE healthcare",
        message="Hi Jordan, ...",
        personalization_rationale="Matches your coverage of AI and healthcare.",
    )
    db.add(draft)
    db.commit()

    evaluation = EvaluationResult(
        artifact_type="outreach_draft",
        artifact_id=draft.id,
        quality_score=91.0,
        checks={"grounding": "PASS", "relevance": "PASS"},
        issues=[],
    )
    db.add(evaluation)
    db.commit()

    assert link.outreach_drafts[0].subject.startswith("Story idea")
    assert evaluation.checks["grounding"] == "PASS"


def test_duplicate_campaign_target_pair_is_rejected():
    db = make_test_session()
    campaign = Campaign(name="Launch", brief="brief text")
    target = Target(
        name="Jordan Rivera",
        category="journalist",
        organization="Gulf Tech Weekly",
        location="Dubai, UAE",
        topics=[],
        industries=[],
        audience=[],
        preferred_themes=[],
        description="desc",
    )
    db.add_all([campaign, target])
    db.commit()

    db.add(
        CampaignTarget(
            campaign_id=campaign.id, target_id=target.id, relevance_score=50.0, matching_reasons=[]
        )
    )
    db.commit()

    db.add(
        CampaignTarget(
            campaign_id=campaign.id, target_id=target.id, relevance_score=60.0, matching_reasons=[]
        )
    )
    try:
        db.commit()
        raised = False
    except Exception:
        db.rollback()
        raised = True

    assert raised, "Expected a uniqueness violation for a duplicate (campaign_id, target_id) pair"
