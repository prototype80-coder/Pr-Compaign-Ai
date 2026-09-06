# Architecture - PR Campaign Copilot

## 1. Overview
Next.js frontend -> FastAPI backend (api/core/models/schemas/services/
repositories) -> SQLite/D1 + AIProvider interface -> CloudflareAIProvider.

## 2. Frontend Architecture
Next.js App Router + TypeScript. app/ = screens, components/ = shared UI,
lib/ = typed API client, types/ = shared types. Explicit loading/empty/
error/success states per page.

## 3. Backend Architecture
api/ = routes only. core/ = config/errors/logging. models/ = SQLAlchemy.
schemas/ = Pydantic I/O + AI validation. services/ = business logic
(CampaignAnalysisService, MatchingService, StoryAngleService,
OutreachService, EvaluationService). repositories/ = DB access per entity.

## 4. Database Architecture
Campaign, Target, CampaignTarget (score + reasons + angle + status),
OutreachDraft, EvaluationResult. SQLite locally, Cloudflare D1 deployed,
standard SQL kept D1-compatible from the start.

## 5. AI Provider Architecture
AIProvider interface: analyze_campaign, generate_story_angle,
generate_outreach, evaluate. CloudflareAIProvider implements it, verified
against live docs before implementation. Final relevance score is always
deterministic code, never LLM output directly.

## 6. Data Flow
POST /campaigns -> analyze -> validate -> persist.
POST /campaigns/{id}/match -> deterministic scoring -> persist.
POST /campaign-targets/{id}/angle -> generate -> validate -> persist.
POST /campaign-targets/{id}/outreach -> generate -> evaluate -> persist both.
PATCH /campaign-targets/{id}/status -> status update only.

## 7. API Boundaries
REST/JSON, resource-oriented endpoints, no GraphQL/websockets.

## 8. Error Handling
Typed AIProviderError -> mapped HTTP errors, no stack traces to users.
Schema validation failures reject rather than best-effort parse. Frontend
has explicit error UI everywhere.

## 9. Testing Strategy
Unit tests for scoring/validation/injection detection (no network).
Integration tests with a stubbed AIProvider. At least one adversarial test.
Frontend tests for happy path + key error states.

## 10. Deployment Architecture
Frontend: Vercel or Cloudflare Pages. Backend: Render or Cloudflare Worker
(decided in Phase 7 after live verification). DB: D1 in prod, SQLite local.

## 11. Security Considerations
No real personal data. Secrets via env vars only. AI output treated as
untrusted: schema-validated, checked for unsupported claims and injection
patterns. Outreach never auto-sent. Limitations documented in AI_SAFETY.md.
