from supabase import create_client, Client
import os

_client: Client | None = None

def supabase() -> Client:
    global _client
    if _client is None:
        _client = create_client(os.getenv("SUPABASE_URL",""), os.getenv("SUPABASE_KEY",""))
    return _client
