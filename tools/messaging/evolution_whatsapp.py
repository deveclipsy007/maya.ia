from agno.tools import tool
import os, requests

class WhatsAppTools:
    @tool
    def send_text(self, phone: str, text: str) -> bool:
        url = f"{os.getenv('EVOLUTION_URL')}/message/sendText/{os.getenv('EVOLUTION_TOKEN')}"
        r = requests.post(url, json={"number": phone, "text": text})
        return r.ok
