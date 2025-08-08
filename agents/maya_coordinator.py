from agno.agent import Agent
from agno.team import Team
from agno.models.openai import OpenAIChat
from agents.patient_agent import patient_agent
from agents.doctor_agent import doctor_agent

maya = Agent(
    name="Maya",
    role="Orquestradora de fluxos médico–paciente",
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions=open("prompts/system_maya.md","r",encoding="utf-8").read(),
    markdown=True,
    show_tool_calls=True,
)

team = Team(
    mode="coordinate",
    members=[patient_agent, doctor_agent],
    model=OpenAIChat(id="gpt-4o-mini"),
    success_criteria="Resolver a intenção do usuário em até 5 passos com confirmação explícita.",
    instructions=[
        "Seja assertiva e clara.",
        "Chame ferramentas apenas quando necessário.",
        "Confirme antes de ações irreversíveis (cancelar/reembolsar).",
    ],
    show_tool_calls=True,
    markdown=True,
)
