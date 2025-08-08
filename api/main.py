from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from agents.maya_coordinator import maya, team
from api.routes import health, appointments, payments, webhooks

# Carrega variáveis do .env automaticamente
load_dotenv()

app = FastAPI(title="Maya API", version="0.1.0")


class ChatRequest(BaseModel):
    message: str


@app.post("/chat/maya")
async def chat_maya(req: ChatRequest):
    """Conversar com a Maya (Agente coordenadora)."""
    try:
        result = maya.run(req.message)
        # result pode ser string ou objeto do Agno; convertemos para string
        return {"reply": str(result)}
    except Exception as e:
        return {"error": str(e)}


# Rotas específicas do domínio
app.include_router(health.router, prefix="/healthz", tags=["health"])
app.include_router(appointments.router, prefix="/appointments", tags=["appointments"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])
app.include_router(webhooks.router, prefix="/webhooks", tags=["webhooks"])
