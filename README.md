# Sample Playwright Python Project

This sample shows a minimal Playwright + Pytest setup with smoke/regression markers and CI examples for GitLab and Jenkins.

## Structure
- tests/ for test cases
- pytest.ini for marker registration
- requirements.txt for dependencies
- .gitlab-ci.yml and Jenkinsfile for CI examples

## Run Locally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 -m playwright install
pytest -m smoke
pytest -m "regression and not smoke"
```
