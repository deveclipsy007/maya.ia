from agno.agent import Agent
from agno.models.openai import OpenAIChat
from tools.supabase_tools import DoctorDBTools
from tools.calendar_tools import CalendarTools
from tools.docs_tools import DocsTools

doctor_agent = Agent(
    name="Atendimento Médico",
    role="Onboarding de médico, agenda, documentos e finanças",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DoctorDBTools(), CalendarTools(), DocsTools()],
    instructions=open("prompts/doctor.md","r",encoding="utf-8").read(),
    markdown=True,
    show_tool_calls=True,
)
