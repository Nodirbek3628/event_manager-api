from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field



class VenuesTypes(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    HYBRID = "hybrid"



class VenueBase(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    location: str = Field(min_length=10, max_length=200)
    venue_type: VenuesTypes 

class VenueCreate(VenueBase):
    pass 

class VenueUpdate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    address: str = Field(min_length=3, max_length=200)
    venue_type: VenuesTypes | None = Field(None)

class VenueOut(VenueBase):
    id: int
    created_at : datetime | None = None
    update_at : datetime | None = None

    class Config:
        from_attributes = True
