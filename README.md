# Sample Playwright Python Project

This sample shows a minimal Playwright + Pytest setup with smoke/regression markers and CI examples for GitLab, Jenkins, and GitHub Actions.

## Structure
- tests/ for test cases
- pytest.ini for marker registration
- requirements.txt for dependencies
- .gitlab-ci.yml, Jenkinsfile, and .github/workflows for CI examples

## Run Locally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 -m playwright install
APP_URL=https://example.com pytest -m smoke
APP_URL=https://example.com pytest -m "regression and not smoke"
```
New Content to trigger Jenkins SCM poll Wed  1 Apr 2026 17:58:29 +08
