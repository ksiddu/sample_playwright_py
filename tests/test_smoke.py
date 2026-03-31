import os
import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
@pytest.mark.regression
def test_home_title(page):
    base_url = os.getenv("APP_URL", "https://example.com")
    expected_title = os.getenv("APP_TITLE", "Example Domain")
    page.goto(base_url, wait_until="domcontentloaded")
    expect(page).to_have_title(expected_title)
