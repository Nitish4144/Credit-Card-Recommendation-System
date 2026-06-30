from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.analytics import DashboardResponse

from app.services.analytics_service import (
    get_dashboard_data,
    get_summary
)

from app.repositories.transaction_repository import (
    get_category_breakdown,
    get_monthly_spend
)

from app.auth.dependencies import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get(
    "/dashboard",
    response_model=DashboardResponse
)
def get_dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_dashboard_data(
        db,
        current_user.id
    )


@router.get("/summary")
def summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_summary(
        db,
        current_user.id
    )


@router.get("/categories")
def categories(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_category_breakdown(
        db,
        current_user.id
    )


@router.get("/monthly")
def monthly(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_monthly_spend(
        db,
        current_user.id
    )