from agno.tools import tool
import os, requests

BASE = "https://api.pagar.me/core/v5"

class PagarmeTools:
    @tool
    def create_checkout(self, amount_cents: int, description: str) -> dict:
        headers = {"Authorization": f"Basic {os.getenv('PAGARME_API_KEY','')}"}
        r = requests.post(f"{BASE}/checkouts", headers=headers,
                          json={"amount": amount_cents, "description": description})
        r.raise_for_status()
        return r.json()
