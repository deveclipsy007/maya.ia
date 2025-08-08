from agno.tools import tool
from services.supabase_client import supabase

class PatientDBTools:
    @tool
    def find_doctors(self, specialty: str|None=None) -> list[dict]:
        q = supabase().table("doctors").select("*").eq("is_approved", True)
        if specialty:
            q = q.ilike("specialty", f"%{specialty}%")
        return q.execute().data

    @tool
    def book_appointment(self, doctor_id: str, patient_id: str, starts_at: str, price_cents: int) -> dict:
        payload = {"doctor_id": doctor_id, "patient_id": patient_id, "starts_at": starts_at,
                   "status": "awaiting_payment", "price_cents": price_cents}
        return supabase().table("appointments").insert(payload).execute().data[0]

    @tool
    def confirm_appointment(self, appointment_id: str, meeting_url: str) -> dict:
        return supabase().table("appointments").update(
            {"status":"confirmed","meeting_url":meeting_url}
        ).eq("id", appointment_id).execute().data[0]

class DoctorDBTools:
    @tool
    def open_slots(self, doctor_id: str, date: str, start: str, end: str, duration_min: int=30) -> int:
        # Exemplo: geraria slots por faixa (mock)
        return 42
