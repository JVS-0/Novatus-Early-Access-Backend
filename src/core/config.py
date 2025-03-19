from enum import Enum
from functools import lru_cache
from logging import INFO
from os import environ
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppEnvironment(str, Enum):
    STAGING = "staging"
    DEVELOPMENT = "development"
    PRODUCTION = "production"


class AppSettings(BaseSettings):
    TITLE: str = "Novatus - Landing Page Backend"
    API_PREFIX: str = "/api"
    VERSION: str = "0.1.0"
    DOCS_URL: str = "/docs"
    IS_ALLOWED_CREDENTIALS: bool = True
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: str = "/redoc"
    HOST: str = environ["SERVER_HOST"]
    PORT: int = int(environ["SERVER_PORT"])
    WORKERS: int = 4
    TIMEZONE: str = "UTC"
    DESCRIPTION: str = ""
    IS_DEBUG: bool = False
    OPENAPI_PREFIX: str = ""
    ALLOWED_ORIGIN_LIST: list[str] = ["*"]
    ALLOWED_METHOD_LIST: list[str] = [
        "GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
    ]
    ALLOWED_HEADER_LIST: list[str] = ["*"]
    LOGGING_LEVEL: int = INFO
    LOGGERS: tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")
    SECRET_KEY: str = "Not So Secret"

    SPREADSHEET_ID: str = environ["SPREADID"]

    model_config = SettingsConfigDict(
        env_file=f"{Path().resolve()}/.env",
        case_sensitive=True,
        validate_assignment=True,
        extra="allow",
    )

    def get_creds(self) -> dict[str, str]:
        return {
            "type": "service_account",
            "project_id": "nino-gdrive",
            "private_key_id": environ["PKEYID"],
            "private_key": environ["PKEY"],
            "client_email": environ["GEMAIL"],
            "client_id": environ["GCLIENTID"],
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": environ["CLIENTX509"],
            "universe_domain": "googleapis.com"
        }

    @property
    def set_app_attributes(self) -> dict[str, str | bool | None]:
        """
        Set all `FastAPI` class' attributes with the custom values defined in `BackendBaseSettings`.
        """
        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "debug": self.IS_DEBUG,
            "description": self.DESCRIPTION,
            "docs_url": self.DOCS_URL,
            "openapi_url": self.OPENAPI_URL,
            "redoc_url": self.REDOC_URL,
            "openapi_prefix": self.OPENAPI_PREFIX,
            "api_prefix": self.API_PREFIX,
        }


class AppStagingSettings(AppSettings):
    ENVIRONMENT: AppEnvironment = AppEnvironment.STAGING
    DESCRIPTION: str = f"Application ({ENVIRONMENT})."
    IS_DEBUG: bool = True


class AppDevelopmentSettings(AppSettings):
    ENVIRONMENT: AppEnvironment = AppEnvironment.DEVELOPMENT
    DESCRIPTION: str = f"Application ({ENVIRONMENT})."
    IS_DEBUG: bool = True


class AppProductionSettings(AppSettings):
    ENVIRONMENT: AppEnvironment = AppEnvironment.PRODUCTION
    DESCRIPTION: str = f"Application ({ENVIRONMENT})."


class FactoryAppSettings:
    def __init__(self, environment: str):
        self.environment = environment

    def __call__(self) -> AppSettings:
        if self.environment == AppEnvironment.PRODUCTION:
            return AppProductionSettings()
        elif self.environment == AppEnvironment.STAGING:
            return AppStagingSettings()
        return AppDevelopmentSettings()


@lru_cache()
def get_settings() -> AppSettings:
    return FactoryAppSettings(environment=environ["APP_ENV"])()


settings = get_settings()
