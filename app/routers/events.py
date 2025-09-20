from fastapi import APIRouter

router = APIRouter(
    prefix="/events",
    tags=["Events"]
)

@router.get("/")
async def mood():
    return {
        "messege": "Alik"
    }