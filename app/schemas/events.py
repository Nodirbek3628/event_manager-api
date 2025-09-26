import enum
from datetime import datetime

from pydantic import BaseModel, Field

class EventTypes(str, enum.Enum):

    CONSERT  = "consert"
    WEDDING  = "wedding"
    WORKSHOP = "workshop"
    SEMINAR  = "seminar" 
    OTHER    = "other"

class EventStatus(str,  enum.Enum):

    DRAFT     = "draft"
    PUBLISHED = "puplished"
    ONGOING   = "ongoing"
    COMPLETED = "complited"
    
class EventBase(BaseModel):
    name: str = Field(min_length=3, max_length=120)
    description: str | None = Field()
    events_type: EventTypes
    adress: str | None = Field()
    status: EventStatus
    start_date: datetime
    end_date: datetime
    venue_id: int
    organizer_id: int

class EventCreate(EventBase):
    pass 

class EventUpdate(BaseModel):
    name: str = Field(min_length=3)
    description: str | None = Field(None,max_length=200)
    events_type: EventTypes | None = Field(None)
    status: EventStatus | None = Field(None)


class EventOut(EventBase):
    id : int
    created_at: datetime | None = None
    updated_at: datetime | None = None
    class Config:
        from_attributes = True
    

    