from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.auth.hashing import hash_password, verify_password
from app.auth.jwt_handler import create_access_token
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserLogin


class AuthService:

    @staticmethod
    def signup(db: Session,user: UserCreate):

        existing_user = UserRepository.get_by_email(db,user.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        hashed = hash_password(user.password)

        created_user = UserRepository.create(
            db,
            email=user.email,
            hashed_password=hashed
        )

        return created_user
    

    @staticmethod
    def login(
        db: Session,
        email: str,
        password: str
    ):

        existing_user = UserRepository.get_by_email(
            db,
            email
        )

        if existing_user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        if not verify_password(
            password,
            existing_user.hashed_password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        token = create_access_token(
            {
                "sub": existing_user.email
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }