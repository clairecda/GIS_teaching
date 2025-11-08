# Week 7 Lecture · Reproducibility & Environments

## Objectives

- Explain why reproducibility matters in spatial analysis (collaboration, auditing, publishing).
- Compare environment management options (dev containers, conda, virtualenv, Colab).
- Introduce best practices for organising projects, documenting dependencies, and versioning data.

## Topics

1. **Reproducibility principles**  
   - Version control (Git), environment capture, data provenance.  
   - Re-running analysis after datasets or boundaries update.
2. **Environment comparison**  
   - Dev containers vs conda vs poetry vs Colab.  
   - Pros/cons, hardware considerations, when to choose each.
3. **Project structure**  
   - Recommended folder layout (mirrors this course).  
   - Naming conventions for raw vs processed data.  
   - `.gitignore` essentials (large rasters, credentials).
4. **Documentation**  
   - README, notebooks with narrative, script comments, automated verification.
5. **Publishing**  
   - Exporting environment specs (`environment.yml`), using `requirements.txt`, Docker images.

## Activities

- Walk through the repository structure highlighting where each artifact lives.  
- Demo `python resources/environment/verify_setup.py` and explain how to extend it.  
- Discuss real-world reproducibility horror stories and prevention strategies.

## Resources

- The Turing Way: *Guide to Reproducible Research*.  
- GitHub docs on Codespaces/devcontainer best practices.
- Course [Environment strategy](../onboarding/environment-options.md) page.
