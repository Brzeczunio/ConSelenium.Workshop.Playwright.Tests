import pytest
from src.configs import PlaywrightConfig, WebsiteConfig
from src.pom.taiga_pom import Taiga
from playwright.sync_api import Page


@pytest.fixture
def playwright_config():
    """Playwright Config fixture"""
    return PlaywrightConfig()

@pytest.fixture
def website_config():
    """Website Config fixture"""
    return WebsiteConfig()

@pytest.fixture
def taiga(page: Page) -> Taiga:
    return Taiga(page)
