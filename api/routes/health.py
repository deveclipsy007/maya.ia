from fastapi import APIRouter

router = APIRouter()

@router.get("")
def health():
    return {"ok": True, "service": "maya", "ts": __import__("datetime").datetime.utcnow().isoformat()}
