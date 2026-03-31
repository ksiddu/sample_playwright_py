import pytest
from playwright.sync_api import expect


@pytest.mark.regression
def test_home_content(page):
    page.goto("https://example.com", wait_until="domcontentloaded")
    heading = page.get_by_role("heading", name="Example Domain")
    expect(heading).to_be_visible()
