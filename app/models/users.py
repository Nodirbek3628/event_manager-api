
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
from database import Base


class UserTypes(str, enum.Enum):
    ADMIN     = "admin"
    ORGANIZER = "organizer"
    USER      = "user"


class Users(Base):
    __tablname__ = "users"
    id       = Column(Integer, primary_key=True,index=True)
    username = Column(String(length=64), unique=True, nullable=False)
    email    = Column(String(length=64), unique=True, nullable=False)
    full_name = Column(String(length=64), nullable=False)
    hashed_password = Column(TEXT,nullable=False)
    user_type = Column(Enum(UserTypes), default=UserTypes.USER, nullable=False)
    create_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    create_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow,nullable=False)

    __table_args__ = (
        CheckConstraint("char_length(username) >= 3", name=("username_min_length")),
        CheckConstraint("char_length(full_name) >= 3", name=("full_name_min_length"))
    )


