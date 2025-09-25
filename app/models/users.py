
from datetime import  datetime
import enum
from sqlalchemy import (
    Integer,
    String,
    TEXT,
    Column,
    DateTime,
    Enum,
    CheckConstraint
)
from sqlalchemy.orm import relationship

from .base import BaseModel


class UserTypes(str, enum.Enum):
    ADMIN     = "admin"
    ORGANIZER = "organizer"
    USER      = "user"


class Users(BaseModel):
    __tablename__ = "users"
    username = Column(String(length=64), unique=True, nullable=False)
    email    = Column(String(length=64), unique=True, nullable=False)
    full_name = Column(String(length=64), nullable=False)
    hashed_password = Column(TEXT,nullable=False)
    user_type = Column(Enum(UserTypes), default=UserTypes.USER, nullable=False)
    events = relationship("Events", back_populates="organizer")

    __table_args__ = (
        CheckConstraint("char_length(username) >= 3", name=("username_min_length")),
        CheckConstraint("char_length(full_name) >= 3", name=("full_name_min_length"))
    )


