# Course Build Checklist

Use this running list to track what has been completed and what still needs attention. Update it as you develop the course.

## Content structure

- [x] Clean root folder structure (`assets/`, `resources/`, `site_docs/`).
- [x] Build MkDocs configuration (`mkdocs.yml`) and base navigation.
- [x] Create lecture pages for Weeks 1–12 (placeholders in 5–12 still need detail).
- [x] Create lab pages for Weeks 1–12 (Weeks 5–12 currently scaffolds).
- [ ] Flesh out Weeks 5–12 lecture pages with full outlines, references, and visuals.
- [ ] Expand Weeks 5–12 lab chapters with detailed instructions, dataset links, and callouts.

## Datasets & resources

- [ ] Populate `resources/docs/data-inventory.md` with confirmed datasets, download dates, and licensing notes.
- [ ] Collect and document Australian sample datasets (crime, health, transport, environmental).
- [ ] Add troubleshooting FAQs for dataset downloads (per week) where needed.

## Visual assets

- [ ] Capture screenshots for Week 1 (interface, project setup) and store under `assets/images/week01/`.
- [ ] Capture symbology/layout examples for Week 2 (`assets/images/week02/`).
- [ ] Gather boundary and join visuals for Week 3 (`assets/images/week03/`).
- [ ] Add terrain analysis outputs for Week 4 (`assets/images/week04/`).
- [ ] Plan visuals for Weeks 5–12 as content is finalised.

## Environment & tooling

- [x] Move environment files to `resources/environment/` and update references.
- [ ] Add troubleshooting FAQ for dev container/conda setup (disk space, SSL issues) in `site_docs/onboarding/environment-options.md`.
- [ ] Record short screen captures for dev container + conda workflows and link them in the onboarding chapter (optional).

## Assessment & capstone

- [ ] Draft Week 11 critique rubric and add to the lecture/lab pages.
- [ ] Write Week 12 capstone brief, deliverables list, and evaluation rubric; link from Week 12 lecture/lab.
- [ ] Add reflection prompts specific to assessments if required.

## Deployment & publishing

- [ ] Decide on hosting (GitHub Pages or other) and add deployment instructions to `README.md`.
- [ ] Verify MkDocs build (`mkdocs build`) for production; ensure no broken links.
- [ ] Consider including a `CONTRIBUTING.md` if other instructors will collaborate.

Refer back to this checklist regularly and mark items off as you complete them. Feel free to add new sections as the course evolves.
