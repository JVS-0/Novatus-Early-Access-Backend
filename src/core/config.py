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

    SPREADSHEET_ID: str = "19qMDZnq1-d00ox7rZ9Axbkh_-bDx_TAwnb0nv8eAssc"

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
            "private_key_id": "0423497896c56c761e207d576d0958a5fd72ca09",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDCqkSYOowHGILl\nzboeAlwyri+gjHcl5bSP6D1A8R0ttqs/OYKQ5ihO4zTqAjNFfFB41cPrkzd7lz4R\nurGdYPPcZDBx+QaMqIR8VE7b13PkCP/Fg4guQhznA6XoogXYyyai4hCzNeknu02i\naUwf8NJkfE0JacuzN8KoT3QwyKocFAzmOqvGHWkQPCavwN8lfc/DmQDQXSOH+ONO\n9wq+++tn4BU6MgfmZHYj4iKEBOMut5LladGmzzRiwjft4zRz9PhCTAM2n8AqNKar\nxkaSzC5N7WOFoZXoSCKJvA1SS4FXQMwxJJ6HWJmRsvmndRxzrnG8IMEmU+yNTlYn\nPAj3YH1HAgMBAAECggEAXWR2+FnOaHEYC8yBqHgVZ7Mt4mbBmwrzb79J8+g5yX7D\n9ddPjtj9KavT7RkVJBcaPH7COjks+zx6aOMa55hmJqximauRutX2ifegxdQ+I381\nxrruENNjLmoPpOZmy7XbWXX/8RrCO2+fNXYzMXfGWLNR+lwpgFgWKc3Evsrm4gTe\nUO+JzAnhbXQvXJtkLBZ3z69aFwJNp1JumVnwZGjyxPxhaYVxnQgYfT5gyaZAfxGO\n+q6WtE/0pRWJnbHUNJDs3USNj5s3D/0GdRg+TBiRqPW+wgFwZWeylHHSKwqVZ1dX\nwrSrvfDnWdOo1YgA3srpKJGOQw0v/4tNgsBKZL2YcQKBgQDkdpNQCi8Q05loYzkO\nbL6+K0szNXyadAi++1Ro37iTrZgwvhrTaQRYh08uji5vaJeuKwckP9Bhst9i85nv\nSw99Oj7EYcjUW4Flky+Knojcm8EyqLFQU7L9ANmyi4zJjpLhQaqgUSiKioZK2e3/\n3bSllD6jNQx61GzJdUbO5N1HswKBgQDaINMGozscj8S4qIMvMGly0z4Kx+Yl5Tf8\nwiqWz/58Cpmmp8YFMoEUCsKuVHSNS+FpW+B9/g5mITiLgsAP+SBaCeFaevIgTA2o\nvg+EaCYXZz0cuMldvSlUqMf8YzYbs+1y35zJxbm6n1LUq2wgOhp+/YoHwkFpHkly\n6s6LC0QqHQKBgE61Exc2CvTvESDHXja7/BKj86pWuPC1HPY+u9vNh1dJLO9N7wv6\nWAbvxrWxQgobrHXSWQmB+pZN+2uppNSttU5dLJaXYYrXY4LM7EoDR/9IoYyEVWHp\nE/bZviYmsYAW4D8+Ujwc+ayRAKb04WuOw9dvdQzhD8WZPUlCX/yTGDDFAoGAUcRS\nNr/Drd462RnaKztTnAaR0ErE/Fmjli1W97e6Ztc2Z+GmelZHSrMJ7X2dP0Y9llgp\nnDE7Ro+XebymsJYryXTAtEE4OGEqEaJFgNXlyYoav4SJf4kkUCcA6JxsMRBOp2wp\ngv2KtOl6jFxCKQZ+3jG+p0/rYzNGRzy79iVgBQUCgYAplE6wkEVgXLwF+K2Akohs\nUld/bqUtRJM3DwLHgBd8YhXzy8V7gDyzsqCJZwHCKiMynTAVtmaW6jUW+e7AHSx6\n3oXAZiGsdSnQkNzxbwEfolqIoG5LTZSlpB3Z1xhgrKNBdSX8RBZ7tdgSvZS27DUb\nutXerDa7SebopAHv+pXgYg==\n-----END PRIVATE KEY-----\n",
            "client_email": "nino-gdrive-service-account@nino-gdrive.iam.gserviceaccount.com",
            "client_id": "117396377688088367467",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/nino-gdrive-service-account%40nino-gdrive.iam.gserviceaccount.com",
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
