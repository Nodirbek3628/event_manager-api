from fastapi import FastAPI

from .dependencies import get_db

from app.models import *
from app.database import Base,engine
from .routers.users import router as users_router
from .routers.events import router as events_router
from .routers.orders import router as orders_router
from .routers.tiskets import router as tiskets_router
from .routers.venues import router as veues_router


app = FastAPI(title="Event_menejer_Api")
Base.metadata.create_all(engine)

app.include_router(users_router)
app.include_router(events_router)
app.include_router(orders_router)
app.include_router(tiskets_router)
app.include_router(veues_router)

