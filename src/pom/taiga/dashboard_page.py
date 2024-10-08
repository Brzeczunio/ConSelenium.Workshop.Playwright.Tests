from src.pom.base_pom import PageObjectModelBase
from playwright.sync_api import expect


class DashboardPage(PageObjectModelBase):
    @property
    def default_url(self):
        return f"{self._env.base_url}"

    @property
    def is_opened(self) -> bool:
        try:
            expect(self._page.get_by_role("navigation")).to_contain_text("Projects")
            return True
        except AssertionError:
            return False