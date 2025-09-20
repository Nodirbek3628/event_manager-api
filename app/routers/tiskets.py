from fastapi import APIRouter

router = APIRouter(
    prefix="/tiskets",
    tags=["Tiskets"]
)

@router.get("/")
async def get_tiskets():
    return "salom"
