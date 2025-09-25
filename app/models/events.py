
import enum
from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    Text,
    Column,
    Enum,
    CheckConstraint,
    ForeignKey,
    DateTime

)
from sqlalchemy.orm import relationship
from .base import BaseModel


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
    

class Events(BaseModel):
    __tablename__ = "events"

    name = Column(String(64), unique=True, nullable=False)
    description = Column(Text) 
    events_type = Column(Enum(EventTypes), default=EventTypes.WEDDING, nullable=False)
    status = Column(Enum(EventStatus), default=EventStatus.DRAFT, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    adress = Column(String(256))
    
    venue_id     = Column(Integer, ForeignKey("venues.id"))
    organizer_id = Column(Integer, ForeignKey("users.id"))

    venue     = relationship("Venues", back_populates="events")
    organizer = relationship("Venues", back_populates="events")

    __table_args__ = (
        CheckConstraint("char_length(name) >= 3", name="event_name_min_length"),
    )
 