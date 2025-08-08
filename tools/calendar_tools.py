from agno.tools import tool
from google.oauth2 import service_account
from googleapiclient.discovery import build
import os, uuid, datetime as dt

SCOPES = ["https://www.googleapis.com/auth/calendar"]
CAL_ID = os.getenv("GOOGLE_CALENDAR_ID", "primary")
CREDS = None
if os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON") and os.path.exists(os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")):
    CREDS = service_account.Credentials.from_service_account_file(
        os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON"), scopes=SCOPES
    )

class CalendarTools:
    @tool
    def create_meet(self, summary: str, starts_at: str, duration_min: int = 30) -> dict:
        if CREDS is None:
            return {"error": "Missing Google credentials"}
        service = build("calendar","v3",credentials=CREDS)
        start = dt.datetime.fromisoformat(starts_at)
        end = start + dt.timedelta(minutes=duration_min)
        body = {
            "summary": summary,
            "start": {"dateTime": start.isoformat()},
            "end": {"dateTime": end.isoformat()},
            "conferenceData": {"createRequest": {"requestId": str(uuid.uuid4())}},
        }
        event = service.events().insert(calendarId=CAL_ID, body=body, conferenceDataVersion=1).execute()
        link = event.get("hangoutLink") or event.get("conferenceData", {}).get("entryPoints", [{}])[0].get("uri")
        return {"event_id": event.get("id"), "meet_link": link}
