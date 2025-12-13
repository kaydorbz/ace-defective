PROJECT REVIEW, CONTEXT & OPERATING PROTOCOLS (Ace Defective)Project Name: Ace DefectiveCurrent Date: December 12, 2025Current Phase: Phase 2 (Content & Identity)1. The Project PurposeAce Defective is a "Man vs. Machine" technical devlog.Primary Goal: Document technical development of the Key2Pee Stealth Project.Secondary Goal: Technical commentary (Pluralistic style) and "The Glitch Report".Monetization: GitHub Sponsors & Ko-fi.2. Executive SummaryThe Infrastructure Layer is COMPLETE.The site is live on Azure Static Web Apps (Free Tier), deployed via a custom Azure DevOps pipeline.Critical Architecture:Hosting: Azure Static Web Apps (West US 2).CI/CD: Azure DevOps (git pro alias triggers build).Build Logic: Manual Build. The pipeline installs Python/Pelican, builds to output/, and deploys that folder directly (skip_app_build: true).Workflow: Work on dev -> Merge to main -> git pro -> Live Site.3. Process & Architecture Fixes (Retrospective)Pipeline Strategy: Switched to app_location: 'output' and skip_app_build: true to bypass Oryx failures.Infrastructure: Manually provisioned via Azure Portal (using "Deployment Token") after CLI subscription issues.Permissions: Explicitly granted "Bypass policies when pushing" to user to allow git pro on main.4. Tech Stack & ConfigurationEngine: Pelican (Python 3.11).Theme: pelican-alchemy.Infrastructure: Azure Static Web Apps (West US 2).CI/CD: Azure DevOps (YAML).Runtime: Python 3.11 (Explicitly pinned).Secrets: AceDefective-Secrets variable group containing AZURE_STATIC_WEB_APPS_API_TOKEN.Domain: acedefective.com (Pending DNS).5. Project RoadmapPhase 1: Infrastructure (COMPLETE)[x] Provisioning: Created Resource Group & Static Web App (Portal).[x] Secrets: Added Deployment Token to Azure DevOps.[x] Pipeline: Finalized azure-pipelines.yml (Manual Build).[x] Deployment: Successful "Green" build via git pro.Phase 2: Content & Identity (ACTIVE)[ ] DNS: Configure acedefective.com CNAME.[ ] Social: Claim handles (Mastodon/Bluesky/Threads).[ ] Content: Post "System Failure: A Manifesto".6. Troubleshoot Documentation (Active Log)IDFeature ContextLocationFailed AttemptsSolutionTS-001Deployment & Security(Pushing via pro alias)Azure DevOpsmain branchAttempt 1: Standard push.• Error: TF402455: Pushes... not permitted.• Reason: Branch Policy blocked direct pushes.Bypass Strategy:Enabled "Bypass policies when pushing" in Branch Security for the specific user account.TS-002Pipeline Build(Building Pelican)azure-pipelines.ymlAttempt 1: Default Oryx build.• Result: Failed to build Pelican.• Reason: Oryx defaults to Node/Python apps, not Pelican.Skip & Script:Used skip_app_build: true and manual script step to run pelican.TS-003Provisioning(Creating Resources)Azure CLIAttempt 1: az group create• Error: "No subscription found".• Reason: Free Trial expired; CLI cached old state.Portal Bypass:Created resources manually via Azure Portal using "Deployment Token" mode.TS-004Git Workflow(Merging Fixes)Local GitAttempt 1: git merge dev• Error: Merge Conflict.• Reason: Concurrent edits to YAML.Resolve Conflict:Used git checkout --theirs to accept the dev version of the pipeline.TS-005Pipeline Deployment(Deploying Artifact)azure-pipelines.ymlAttempt 1: app_location: '/'• Error: "Failed to find default file".• Reason: Azure looked in root, but build was in output.Path Correction:Updated YAML to set app_location: 'output' and output_location: ''.Appendix A: Current File StructurePlaintextace-defective/
├── .github/
│   └── FUNDING.yml
├── staticwebapp.config.json    # Security Headers
├── azure-pipelines.yml         # [Stable] Manual Build + Python 3.11
├── content/
│   ├── articles/
│   │   └── system-failure-manifesto.md
├── pelicanconf.py
├── publishconf.py
├── requirements.txt
└── .gitignore
Appendix B: Development ProtocolsI. Technical GuardrailsNever Commit output/: The pipeline builds the site; do not commit the generated HTML.Content Workflow: Write posts in content/ on the dev branch. Preview locally using pelican --listen.Secrets: Ensure no API keys (if added later) are in pelicanconf.py.Dual Push: Use the pro alias for pushes to main.Appendix C: Full Codebase Ingest ProtocolRun this PowerShell script in the ace-defective directory to generate a full context dump (codebase_dump.txt).PowerShell$outputFile = "codebase_dump.txt"
$files = @(
    "pelicanconf.py",
    "publishconf.py",
    "requirements.txt",
    ".gitignore",
    "azure-pipelines.yml"
)

"ACE DEFECTIVE CODEBASE CONTEXT" | Out-File $outputFile -Force -Encoding UTF8

foreach ($f in $files) {
    "`n--- START OF FILE: $f ---" | Out-File $outputFile -Append
    if (Test-Path $f) {
        Get-Content $f | Out-File $outputFile -Append
    } else {
        "File not found: $f" | Out-File $outputFile -Append
    }
    "--- END OF FILE: $f ---" | Out-File $outputFile -Append
}
Write-Host "Context saved to $outputFile" -ForegroundColor Green
