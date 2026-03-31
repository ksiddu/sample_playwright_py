import os
import pytest
from playwright.sync_api import expect


@pytest.mark.regression
def test_home_content(page):
    base_url = os.getenv("APP_URL", "https://example.com")
    expected_heading = os.getenv("APP_HEADING", "Example Domain")
    page.goto(base_url, wait_until="domcontentloaded")
    heading = page.get_by_role("heading", name=expected_heading)
    expect(heading).to_be_visible()
