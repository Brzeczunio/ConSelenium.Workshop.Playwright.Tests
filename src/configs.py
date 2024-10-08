import pydantic_settings


class PlaywrightConfig(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_prefix="QA_PLAYWRIGHT_",
        env_file=".env",
        frozen=True,
        extra="ignore"
    )

    headless: bool = True
    browser: str = ""

class WebsiteConfig(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_prefix="QA_SITE_SETTINGS_",
        env_file=".env",
        frozen=True,
        extra="ignore"
    )

    base_url: str = ""
    username: str = ""
    password: str = ""