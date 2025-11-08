# Course Roadmap

Use this roadmap to plan development and delivery milestones as you build out the course.

## Development milestones

1. **Finalize syllabus:** lock the 12-week outline, learning goals, assessments, and reflection prompts.
2. **Author QGIS guides (Weeks 1–6):** include screenshots, dataset links, and troubleshooting sections.
3. **Publish onboarding materials:** QGIS install guide, data download instructions, environment strategy, boundary explainer.
4. **Build managed environment assets:** dev container, `environment.yml`, verification script, Colab fallback notebooks.
5. **Draft Python module guides (Weeks 7–10):** align with notebooks and dataset structure.
6. **Design studio & capstone materials:** layout critique checklist, capstone brief, evaluation rubric.
7. **Collect datasets:** download, clean, and document sources in the data inventory; store staged copies where licensing allows.
8. **Pilot test:** run through selected weeks with learners or colleagues to gather feedback and refine pacing.
9. **Publish site:** deploy MkDocs site (e.g., GitHub Pages) and update README with deployment instructions.
10. **Iterate:** track feedback/issues, update documentation, and maintain dependencies.

## Suggested weekly cadence

- **Week 0 (orientation):** ensure all learners have the course book, QGIS installed, datasets downloaded, and reflections ready.
- **Weekly cycle:** release readings and data instructions mid-week, host synchronous session or lab, assign optional practice/reflection.
- **Checkpoints:** Weeks 4, 8, and 11 can serve as internal check-ins or mini-assessments leading up to the capstone.

## Publishing checklist

- [ ] MkDocs site builds locally (`mkdocs serve`) without warnings.
- [ ] All internal links resolve (datasets, reflections, notebooks).
- [ ] `mkdocs.yml` navigation reflects the final structure.
- [ ] LICENSE files added and referenced in the course book.
- [ ] GitHub Pages (or preferred host) configured, and base URL tested.
- [ ] README updated with instructions to build the docs (`mkdocs build`) and preview (`mkdocs serve`).

Keep this roadmap up to date as you expand the course or onboard additional instructors.
