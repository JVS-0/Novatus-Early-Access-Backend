from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build # type: ignore


from src.models.schema.early_access import EarlyAccessRegistration


def get_sheets_service(credentials: dict[str, str]): # type: ignore
    """
    Build and return a Google Sheets service using JSON from environment.
    """

    creds = Credentials.from_service_account_info( # type: ignore
        credentials,
        scopes=["https://www.googleapis.com/auth/spreadsheets"],
    )

    return build("sheets", "v4", credentials=creds) # type: ignore


def append_row_to_google_sheet(spreadsheet_id: str, credentials: dict[str, str], data: EarlyAccessRegistration):
    """
    Append a row to the configured Google Sheet using the Sheets API.
    The row is: [Registration Date, Name, Email, Mobile, Message].
    """
    sheet = get_sheets_service(credentials=credentials).spreadsheets() # type: ignore

    values = [[ # type: ignore
        data.registered_at.isoformat(),
        data.name,
        data.email,
        data.mobile or "",
        data.msg or ""
    ]]
    body = {"values": values} # type: ignore

    result = sheet.values().append( # type: ignore
        spreadsheetId=spreadsheet_id,
        range="Sheet1!A:E",
        valueInputOption="RAW",  # or 'USER_ENTERED' if you want Sheets to auto-format
        insertDataOption="INSERT_ROWS",
        body=body
    ).execute() # type: ignore
