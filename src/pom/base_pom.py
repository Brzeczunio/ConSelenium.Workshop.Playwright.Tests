import playwright.sync_api as playwright
from src import configs


class PageObjectModelBase:
    def __init__(self, page: playwright.Page):
        self._page = page
        self._env: configs.WebsiteConfig = configs.WebsiteConfig()
        self._playwright: configs.PlaywrightConfig = configs.PlaywrightConfig()

    @property
    def default_url(self):
        raise NotImplemented

    @property
    def page(self):
        return self._page

    def goto(self):
        self._page.goto(self.default_url)

    def pause(self):
        self._page.pause()