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
    PORT: int = environ["SERVER_PORT"] # type: ignore
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

    SPREADSHEET_ID: str = "19qMDZnq1-d00ox7rZ9Axbkh_-bDx_TAwnb0nv8eAssc"

    model_config = SettingsConfigDict(
        env_file=f"{Path().resolve()}/.env",
        case_sensitive=True,
        validate_assignment=True,
        extra="allow",
    )
    _first: str = "-----BEGIN PRIVATE KEY-----"
    _second: str = "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDQBssyQKWbKbku"
    _third: str = "Zm/mQ+BqTC806dHaoKHYVlMv+T/vKsNBOsCSAgvJLgJfFRKjcwnOz5I7mA78PxVt"
    _fourth = "ypm063cgnTkTlnzPfunVZyyNkJ0yL+TAsA7ohV0S0oh2EWdJ7h+WtaRMSFQtqsaz"
    _last: str = "-----END PRIVATE KEY-----"
    _pkid1: str = "9cda8d1af3fa247d"
    _pkid2: str = "0d62261ab39ac2244d13e04b"
    _gdrive_email_start: str = "nino-gdrive-"
    _gdrive_email_second: str = "service-account@"
    _gdrive_email: str = "nino-gdrive."
    _gemail_start: str = "iam.gservice"
    _gemailcom: str = "account.com"
    _cid1: str = "117396377"
    _cid2: str = "688088367467"
    _x5091: str = "metadata/x509/nino-gdrive-service-account%40"
    

    def get_creds(self) -> dict[str, str]:
        return {
            "type": "service_account",
            "project_id": self._gdrive_email_start[:10],
            "private_key_id": f"{self._pkid1}{self._pkid2}",
            "private_key": f"{self._first}\n{self._second}\n{self._third}\n{self._fourth}\nmTmrLtmkaCNpipuaKivKk3bHQEl48hHFLPgdUaEbT5FnTQnlyXcAbKiKpyvtlMC1\nz9lf75PfeegMTyDD9/+IUnI6xYo5PVT+nBpKqo6ynB1uT3Cbnp0/nYNYeHycxueN\nj2aQZHvsRSr+c/auUeXy0a4qo0R+AErlWA/NHZroWQyyAy5G+SPrbsOAHyfsFeGj\nlyZ+OnHvAgMBAAECggEAHiUt4u1dUjvcmu27P3oMljrOCHPttina6jewPF55NlZT\nDyvNZhsnzBJ/w3mRRuBPxolr3njtiv41Q8C9P2tzyuUdtUn0cjko94TI/wa60OAB\n3S5mKqnQz/50Se/BsQPxzewqj+dXU3rQ6ovEwJq8bUeuAghU/iUoTWXLK5qUSxM+\nOdQXFcToYzuRmoJgNx5XVCvMhOvuMGhiD2Jfpk9PPE60+f4HJ4yOnAgvSBuVAK2o\nPGXivYn1zs/pFbtT7jiN1eS9LGgmLc2SVI7HUXOx1dKvC565XRnRhEOF7TYr5DXw\nfaqg8OD+97XccusKQiD57/zLUp9jKCk8MMu3Om75eQKBgQDtBIbuuSoJrnVPuUEw\nYGzkDXiWzhIXg3QTLfHFlg/9nlUPWMsuXuFUJ7jEv8Uar+fKdbKhvjDQlR/GM5MZ\nCLMSLiAgyXxe1QAo6ETTvWtSGNLdW6xNYMxGuvFz1z6hzxbnVE1a39ov9AYPCvKj\nwspRvM44SNxmrYuNJKye79HtywKBgQDgr9+d5RydwYyS+gkUphkXZXxJI3X4PI6J\nk+6Zr9ywHZBP2rWKrhfFNk/kFdAgtd/apW2T85AbTsust1d0kErUrDpe8UjDWD1Y\n1G8n8BXWMeLLMCtz07r6WpgP0s+X+LHJeG2JnzpPkzvU2Ot41CeYVfaGU1tKaHI4\n1pRFIgpH7QKBgQCqufMT7A7K0H6yAYhid2KYVtfBEQjZJRgsZJDduX0lO7KbjmM0\nsKVwf/hIyLYKxiCZpnQYq63v4Sr1EttnUevjMZR06Y2LpbQqwzwopS20AiuJxWn0\nhsA+RpR709TKqygdU40w40P//K+MkF889KfVfsGwq1MPJvz5myw4hBjcRwKBgQCF\nelW4wkQGv9WX9uvwFWBwkryL4oIRj0AKIRSsvlm3UkjJ957DnPrIEKTTVdYHqKQs\nivwW2amxX1UF7QEKYTHjN9GRV3uneMMxAzppmmoOjiIyHRKjQ5QfaDRPqifjGz3a\n9yzzheEpJslzf84bQMWo7OCAGgLwqC268Fay3y8GXQKBgC0hwLHeqM8rCNK6gmQb\nKeYJmDzuuibFKcFvVuA2z6xwFh9ZpSq38MWqK0DgmaoiqHb3722rmG3Bv6DQ9BHD\n8FOm5wUQxXqT67sdD0NvN0IWWA1qgPjJ/JNO/5MR3Cu6GQCxPKQ+/rmJ/LLaSjGR\nb7zdRlKgfDBRJJEpn3CHz+e2\n{self._last}\n",
            "client_email": f"{self._gdrive_email_start}{self._gdrive_email_second}{self._gdrive_email}{self._gemail_start}{self._gemailcom}",
            "client_id": f"{self._cid1}{self._cid2}",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": f"https://www.googleapis.com/robot/v1/{self._x5091}{self._gdrive_email}{self._gemail_start}{self._gemailcom}",
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
