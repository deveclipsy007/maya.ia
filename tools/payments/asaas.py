from agno.tools import tool
import os, requests

ASAAS_API = "https://api.asaas.com/v3"
HEAD = {"access_token": os.getenv("ASAAS_API_KEY","")}

class AsaasTools:
    @tool
    def create_payment_link(self, customer_id: str, value: float, description: str) -> dict:
        r = requests.post(f"{ASAAS_API}/paymentLinks", headers=HEAD,
                          json={"name": description, "chargeType":"DETACHED", "value": value,
                                "description": description, "billingType":"UNDEFINED"})
        r.raise_for_status()
        data = r.json()
        return {"payment_link": data.get("url"), "payment_link_id": data.get("id")}
