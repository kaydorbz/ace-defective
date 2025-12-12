PROJECT REVIEW, CONTEXT & OPERATING PROTOCOLS (Ace Defective)Project Name: Ace DefectiveCurrent Date: December 11, 2025Current Phase: Phase 2 (Content & Configuration)1. Executive SummaryAce Defective is a technical blog/devlog built to track the development of Key2Pee and other projects, styled after Pluralistic. The site is generated using Pelican (Python) and hosted on Azure Static Web Apps.Current Status: Infrastructure is fully operational. A CI/CD pipeline (GitHub Actions) automatically builds and deploys the Pelican site upon commits to main. We are ready to configure the site metadata and write the first content.2. Process & Architecture Fixes (Retrospective)Pipeline Established: GitHub Actions workflow created to handle the Pelican build and deployment.Theme Installation: pelican-alchemy installed via source to resolve PyPI issues.Dual Repositories: Project managed across GitHub (source control, CI/CD trigger) and Azure DevOps (mirror/project management).Shortcut Protocol: The custom Git alias pro is established.3. Tech Stack & ConfigurationEngine: Pelican (Python Static Site Generator).Theme: pelican-alchemy.Infrastructure: Azure Static Web Apps (Free Tier).Deployment: GitHub Actions (CI/CD).Content Format: Markdown / ReStructuredText.4. Git Workflow StatusRepositories: GitHub (Primary Source/CI) and Azure DevOps (Secondary/PM).main Branch: STABLE. Connected to Azure Production.dev Branch: ACTIVE. Used for drafting posts or theme tweaks.pro Shortcut: The Git alias pro executes: $git\ push\ azure\ main\ \&\&\ git\ push\ origin\ main$.5. Next Immediate Actions (Phase 2)Site Metadata: Update pelicanconf.py with the actual blog name, author, and social links.First Post: Create the inaugural "Hello World" article in the content/ directory.Pipeline Verification: Confirm the first content change successfully updates the live site.Appendix A: Current File Structure(Pelican/Azure Static Web Apps Template)Plaintextace-defective/
├── .github/
│   └── workflows/
│       └── azure-static-web-apps.yml  # The CI/CD Pipeline
├── content/                    # Where your Markdown posts live
│   └── images/
├── output/                     # (Ignored) Generated HTML
├── themes/
│   └── pelican-alchemy/
├── pelicanconf.py              # Main Settings (Title, Links, Author)
├── publishconf.py              # Production Settings
├── requirements.txt            # Python dependencies
└── .gitignore
Appendix B: Development ProtocolsI. Technical GuardrailsNever Commit output/: The pipeline builds the site; do not commit the generated HTML.Content Workflow: Write posts in content/ on the dev branch. Preview locally using pelican --listen.Secrets: Ensure no API keys (if added later) are in pelicanconf.py.Dual Push: Use the pro alias for pushes to main.Appendix C: Full Codebase Ingest ProtocolRun this PowerShell script in the ace-defective directory to generate a full context dump (codebase_dump.txt).PowerShell$outputFile = "codebase_dump.txt"
$files = @(
    "pelicanconf.py",
    "publishconf.py",
    "requirements.txt",
    ".gitignore",
    ".github/workflows/azure-static-web-apps.yml"
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
