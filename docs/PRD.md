# Product Requirements Document - PR Campaign Copilot

## 1. Problem
PR professionals starting a new campaign face a research bottleneck: given a
campaign idea, they must manually figure out who to target, why those
targets are relevant, what angle to pitch, and how to personalize outreach,
while staying grounded in facts they can actually support.

## 2. Target Users
- PR professionals / agencies planning a campaign.
- (Secondary) A hiring evaluator assessing engineering judgment.

## 3. Product Goal
Turn a free-text campaign brief into an explainable outreach strategy:
relevant targets, transparent match reasoning, grounded story angles, and
human-reviewable outreach drafts, backed by an AI quality-control layer.

## 4. MVP Scope
1. Campaign intake (brief + optional fields).
2. AI campaign analysis into structured schema.
3. Fictional dataset of ~30-50 PR targets across categories.
4. Deterministic, transparent target-matching/scoring.
5. AI-generated story angles grounded in campaign + target data.
6. AI-generated editable outreach drafts.
7. Outreach status tracking, persisted.
8. AI evaluation/quality-control layer.
9. At least one adversarial/failure case, documented in AI_SAFETY.md.
10. Core screens: Dashboard, Create Campaign, Campaign Overview, Target
    Recommendations, Target Detail, Outreach Review, Evaluation Panel.

## 5. User Workflow
Brief -> structured analysis -> ranked targets with reasons -> story angle
-> outreach draft + evaluation -> human review -> status update.

## 6. Functional Requirements
FR1 create/list/view campaigns. FR2 validated campaign analysis. FR3 seed &
query targets. FR4 documented scoring with stored reasons. FR5 grounded
story angles. FR6 editable outreach drafts. FR7 persisted status. FR8
evaluate all AI artifacts. FR9 surface evaluation failures. FR10 handle
adversarial input.

## 7. Non-Functional Requirements
NFR1 free-tier only. NFR2 AIProvider abstraction. NFR3 env-var secrets. NFR4
graceful AI failure handling. NFR5 schema validation before persistence.
NFR6 real loading/empty/error states. NFR7 tests for scoring/validation/
adversarial cases.

## 8. AI-Specific Requirements
Score is deterministic, never LLM-invented. No unsupported claims. Every
artifact passes evaluation before shown as ready. Adversarial case
demonstrated and documented.

## 9. Constraints
Zero/near-zero cost, Cloudflare free tier preferred, no credit card unless
flagged first, verify live Cloudflare capabilities before implementing.

## 10. Success Criteria
End-to-end brief-to-outreach flow works; every target shows a reason;
adversarial case is caught; small reviewable commits; runs on free tier.

## 11. Explicitly Excluded from MVP
Real scraped data, multi-user auth, actual email sending, analytics
dashboards, multiple simultaneous providers, the what-if simulator (stretch
only), production-grade auth/rate-limiting/monitoring.
