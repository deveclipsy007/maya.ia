from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools
from tools.supabase_tools import PatientDBTools
from tools.calendar_tools import CalendarTools
from tools.payments.asaas import AsaasTools
from tools.payments.pagarme import PagarmeTools
from tools.messaging.evolution_whatsapp import WhatsAppTools
from tools.docs_tools import DocsTools
import os

payment_tool = AsaasTools() if os.getenv("PAYMENT_PROVIDER","asaas")=="asaas" else PagarmeTools()

patient_agent = Agent(
    name="Atendimento Paciente",
    role="Agendar, remarcar, cancelar; gerar pagamento; confirmar; criar Meet; pós-consulta",
    model=OpenAIChat(id="gpt-4o"),
    tools=[ReasoningTools(add_instructions=True), PatientDBTools(), payment_tool, CalendarTools(), WhatsAppTools(), DocsTools()],
    instructions=open("prompts/patient.md","r",encoding="utf-8").read(),
    markdown=True,
    show_tool_calls=True,
)
