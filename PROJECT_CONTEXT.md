# PROJECT REVIEW, CONTEXT & OPERATING PROTOCOLS

**Project Name:** Ace Defective
**Current Date:** December 11, 2025
**Current Phase:** Phase 1 (Infrastructure & Scaffolding)

## 1. Executive Summary
The project has successfully generated the site skeleton using Pelican. We are currently configuring the local Git repository and preparing for the first push to Azure. The "Man vs. Machine" devlog structure is established.

## 2. Process & Architecture Fixes (Retrospective)
* **Troubleshooting:** `pip install` for the theme failed due to a missing PyPI package. Fixed by installing directly from the GitHub source URL.
* **Protocols:** Established "Master Project Context" (MPC) and strict "Security First" .gitignore rules.

## 3. Tech Stack & Configuration
* **Frontend/Engine:** Pelican (Python Static Site Generator).
* **Theme:** `pelican-alchemy` (Installed via Source).
* **Infrastructure:** Azure Static Web Apps (Free Tier).
* **Shell:** PowerShell.

## 4. Git Workflow Status
* **`main` Branch:** PENDING (Will contain stable skeleton).
* **`dev` Branch:** PENDING (Will be active work branch).

## 5. Next Immediate Actions (Phase 1)
1.  Initialize Git.
2.  Commit the skeleton to `main`.
3.  Create and switch to `dev`.
4.  Push to GitHub.

## Appendix A: Development Protocols
1.  **Security First:** Never commit secrets. Verify `.gitignore`.
2.  **Branch Discipline:** Keep `main` stable. Merge `dev` only when a Phase is complete.
3.  **Review Before Write:** Always request current code context before editing core files.