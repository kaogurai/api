from fastapi import APIRouter

router = APIRouter(
    prefix="/emoji",
    tags=["emoji"],
)


@router.get("/")
def root():
    return {
        "detail": "This is the base URL for the emoji endpoints. Check the documentation for more information."
    }
