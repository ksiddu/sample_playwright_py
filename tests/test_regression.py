import os
import pytest
from playwright.sync_api import expect


def open_home(page):
    base_url = os.getenv("APP_URL", "https://example.com")
    expected_heading = os.getenv("APP_HEADING", "Example Domain")
    response = page.goto(base_url, wait_until="domcontentloaded")
    return response, base_url, expected_heading


@pytest.mark.regression
def test_home_content(page):
    _, _, expected_heading = open_home(page)
    heading = page.get_by_role("heading", name=expected_heading)
    expect(heading).to_be_visible()


@pytest.mark.regression
def test_home_status_code_is_success(page):
    response, _, _ = open_home(page)
    assert response is not None
    assert response.ok
    assert response.status == 200


@pytest.mark.regression
def test_home_has_single_main_heading(page):
    _, _, expected_heading = open_home(page)
    heading = page.get_by_role("heading", name=expected_heading)
    expect(heading).to_have_count(1)


@pytest.mark.regression
def test_home_url_matches_target(page):
    _, base_url, _ = open_home(page)
    assert page.url.rstrip("/") == base_url.rstrip("/")
