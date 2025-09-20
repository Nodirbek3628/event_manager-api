from fastapi import APIRouter

router = APIRouter(
    prefix="/venues",
    tags=["Venues"])

@router.get("/")
async def get_venues():
    return "Qiymat"