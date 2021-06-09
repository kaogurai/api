from fastapi import APIRouter

router = APIRouter(
    prefix="/tts",
    tags=["tts"],
)


@router.get("/")
def root():
    return {"message": "TTS Endpoints"}
