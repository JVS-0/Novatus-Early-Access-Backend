from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.core.config import settings
from src.models.schema.early_access import EarlyAccessRegistration
from src.utils.gdrive_handler import append_row_to_google_sheet

router = APIRouter(tags=["Early Access Registration"])


@router.post(
    path="/register_early_access",
    response_class=JSONResponse,
    name="early-access:registration",
    status_code=status.HTTP_200_OK,
)
async def register_early_access(registration: EarlyAccessRegistration):
    """
    Endpoint for early access registration.
    Appends the data to an Excel sheet on Google Drive (or anywhere else).
    """
    append_row_to_google_sheet(
        spreadsheet_id=settings.SPREADSHEET_ID,
        credentials=settings.get_creds(),
        data=registration
    )
    return JSONResponse(content={"message": "Registration successful!"})
