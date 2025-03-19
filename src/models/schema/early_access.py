from datetime import datetime
from typing import Optional

from src.models.schema.base import BaseSchemaModel

class EarlyAccessRegistration(BaseSchemaModel):
    name: str
    email: str
    mobile: Optional[str] = None
    msg: Optional[str] = None
    registered_at: datetime
