from fastapi import APIRouter, Request
from services.supabase_client import supabase

router = APIRouter()

@router.post("/asaas")
async def asaas_webhook(req: Request):
    body = await req.json()
    event = body.get("event")
    payment = body.get("payment", {})
    if event in {"PAYMENT_CONFIRMED","PAYMENT_RECEIVED"}:
        appointment_id = payment.get("externalReference")
        if appointment_id:
            supabase().table("appointments").update({"status":"confirmed"}).eq("id", appointment_id).execute()
    return {"ok": True}

@router.post("/pagarme")
async def pagarme_webhook(req: Request):
    body = await req.json()
    # TODO: mapear status pagos/refundados/falhos
    return {"ok": True}
