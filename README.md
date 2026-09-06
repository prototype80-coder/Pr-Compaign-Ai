# PR Campaign Copilot

Turns a PR campaign brief into an explainable outreach strategy: relevant
targets with transparent match reasoning, grounded story angles, and
human-reviewed personalized outreach drafts, backed by an AI
quality-control layer.

Built as a technical assessment. See docs/PRD.md for scope and
docs/ARCHITECTURE.md for how it's put together.

## Status
In progress - repository scaffolding stage.

## Project Structure
backend/  FastAPI app (api / core / models / schemas / services / repositories)
frontend/ Next.js + TypeScript UI
data/     Fictional sample target dataset
docs/     PRD, architecture, AI safety, evaluation docs

## Setup

### Backend
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp ../.env.example ../.env
uvicorn app.main:app --reload

### Frontend
cd frontend
npm install
cp ../.env.example .env.local
npm run dev

### Tests
cd backend
pytest

## Development Principle
AI writes the code. The engineer owns the outcome. Every phase is built
incrementally, reviewed, tested, and committed before moving to the next.
