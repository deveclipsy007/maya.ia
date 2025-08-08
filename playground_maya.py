# Playground da Maya com memória/storage em Postgres (Agno)
# Executa uma aplicação Playground na porta 7777
# Requer: OPENAI_API_KEY e DATABASE_URL no ambiente (.env já é carregado)

from dotenv import load_dotenv
load_dotenv()

from agno.playground import Playground
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.memory.agent import AgentMemory
from agno.memory.db.postgres import PgMemoryDb
from agno.storage.postgres import PostgresStorage
import os

# DATABASE_URL deve ser algo como:
# postgresql+psycopg://USER:PASSWORD@HOST:PORT/DBNAME
# Ex.: postgresql+psycopg://postgres:YOUR_PASSWORD@db.xxxxx.supabase.co:5432/postgres?sslmode=require
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL não definido. Configure no .env antes de iniciar o Playground.")

# Importa a Maya já configurada
from agents.maya_coordinator import maya

# Opcionalmente, você pode garantir o modelo aqui (mantemos o do arquivo do agente)
assert isinstance(maya, Agent)

# Anexa memória e storage persistentes à Maya
maya.memory = AgentMemory(
    db=PgMemoryDb(
        table_name="agent_memory",
        db_url=DATABASE_URL,
    ),
    create_user_memories=True,
    update_user_memories_after_run=True,
    create_session_summary=True,
    update_session_summary_after_run=True,
)

maya.storage = PostgresStorage(
    table_name="agent_sessions",
    db_url=DATABASE_URL,
    auto_upgrade_schema=True,
)

# Cria o Playground App com a Maya
playground = Playground(
    agents=[maya],
    name="Maya",
    description="Playground da Maya (coord) com memória Postgres",
    app_id="maya-playground",
)

app = playground.get_app()

if __name__ == "__main__":
    # Porta padrão do Playground é 7777
    playground.serve(app="playground_maya:app", host="127.0.0.1", port=7777, reload=True)
