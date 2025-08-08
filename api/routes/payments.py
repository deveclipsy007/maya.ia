from fastapi import APIRouter, HTTPException, Body
from tools.payments.asaas import AsaasTools
from tools.payments.pagarme import PagarmeTools
import os

router = APIRouter()

@router.post("/link")
def create_payment_link(payload: dict = Body(...)):
    provider = os.getenv("PAYMENT_PROVIDER","asaas")
    value = payload.get("value")
    description = payload.get("description","Consulta Hopecann")
    customer_id = payload.get("customer_id","")
    if not value:
        raise HTTPException(400, "value é obrigatório")
    tool = AsaasTools() if provider == "asaas" else PagarmeTools()
    if provider == "asaas":
        return tool.create_payment_link(customer_id=str(customer_id), value=float(value), description=description)
    else:
        return tool.create_checkout(amount_cents=int(value*100), description=description)
