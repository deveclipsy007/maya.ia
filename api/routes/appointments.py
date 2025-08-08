from fastapi import APIRouter, HTTPException, Body
from services.supabase_client import supabase

router = APIRouter()

@router.post("")
def create_appointment(payload: dict = Body(...)):
    # Espera: patient_id, doctor_id, starts_at, price_cents
    req = {k: payload.get(k) for k in ["patient_id","doctor_id","starts_at","price_cents"]}
    if not all(req.values()):
        raise HTTPException(400, "Campos obrigatórios ausentes")
    req["status"] = "awaiting_payment"
    data = supabase().table("appointments").insert(req).execute().data[0]
    return {"ok": True, "appointment": data}
