from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.users import Users
from app.schemas.users import UserCreate, UserOut


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(Users).all()
    return users

@router.post("/", response_model=UserOut)
async def create_users(user:UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(Users).filter((Users.username == user.username)| (Users.email == user.email)).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already exists "
    )

    db_users = Users(
        username = user.username,
        email = user.email,
        full_name = user.full_name,
        user_type = user.user_type,
        hashed_password = user.hashed_password
    )
    db.add(db_users)
    db.commit()
    db.refresh(db_users)
    return db_users


@router.get("/{user_id}", response_model=UserOut)
async def change_user_type(user_id: int, new_type: str, db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    user.user_type = new_type
    db.commit()
    db.refresh(user)
    return user