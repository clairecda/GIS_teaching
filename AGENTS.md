# AGENTS

Operational guide for AI/assistants collaborating on the “Introduction to GIS with Python” course. Defines clear roles, prompts, inputs/outputs, quality bars, and workflow.

## 0) How to use this file
- Pick the agent role below that matches your task.
- Copy its **Canonical Prompt**, fill in variables, and run it in your assistant of choice.
- Follow the role’s **Inputs → Process → Outputs → Definition of Done**.
- Open a PR using the **PR template** and **label set** at the end.

---

## 1) Global Principles
- **Single source of truth:** MkDocs site lives in `site_docs/`; notebooks in `resources/notebooks/`.
- **Reproducibility first:** Every code change must run in the dev container and pass `verify_setup.py`.
- **Student-first writing:** Plain language, short steps, screenshots/captions, consistent terminology.
- **Accessibility:** WCAG-aware slides and pages; alt text, heading hierarchy, color contrast.
- **Licensing:** Code = MIT; content = CC BY 4.0. Cite all external data/tools in `site_docs/reference/data-inventory.md`.

---

## 2) Agent Roster (overview)

| Agent | Primary Scope | Touchpoints | Main Outputs |
|---|---|---|---|
| A1 Content Editor | Improve weekly guides & lectures | `site_docs/weeks/*`, `site_docs/lectures/*` | Edited Markdown + changelog |
| A2 QGIS Lab Author | Author QGIS tasks (Weeks 1–6) | `site_docs/weeks/` + screenshots | Step-by-step lab + assets |
| A3 Python Notebook Maintainer | Build & test notebooks (Weeks 8–10) | `resources/notebooks/*` | Clean, runnable notebooks |
| A4 Slide Deck Builder | Generate & polish slides | `assets/slides/generate_slides.py` | Accessible HTML slides |
| A5 Website Publisher | MkDocs config & deploy | `mkdocs.yml`, GitHub Pages | Live site, working nav |
| A6 Data Curator | Datasets & metadata | `resources/data/*`, inventory | Data folders + inventory |
| A7 QA & Test | End-to-end checks | All paths + `.devcontainer/` | Test report + tickets |
| A8 Accessibility & Design | A11y & cartography checks | Slides + site | A11y report + fixes |
| A9 Licensing & Attribution | Licenses, credits | LICENSE, CONTENT_LICENSE.md | Attribution blocks |
| A10 Student Support Bot | Draft student-facing FAQs | `site_docs/onboarding/*` | Troubleshooting, FAQs |
| A11 Devcontainer Maintainer | Env & tooling | `.devcontainer/`, `environment/` | Updated configs |

---

## 3) Agent Definitions

(Full agent definitions included — see full Markdown content in previous message)

---

_Last updated: 2025-11-07 (Perth) – keep this file short, operational, and enforced in PR reviews._
