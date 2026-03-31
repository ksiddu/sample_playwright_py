import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
@pytest.mark.regression
def test_home_title(page):
    page.goto("https://example.com", wait_until="domcontentloaded")
    expect(page).to_have_title("Example Domain")
