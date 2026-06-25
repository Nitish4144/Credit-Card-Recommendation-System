from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.analytics import DashboardResponse

from app.services.analytics_service import (
    get_dashboard_data,
    get_category_breakdown,
    get_monthly_spend,
    get_summary,
    get_total_spend,
    get_transaction_count

)

router  = APIRouter(prefix="/analytics" , tags =["Analytics"])

@router.get(
    "/dashboard",
    response_model = DashboardResponse
)
def get_dashboard(
    db: Session = Depends(get_db)
):
    return get_dashboard_data(db)

@router.get("/summary")
def summary(
    db: Session = Depends(get_db)
):
    return get_summary(db)

@router.get("/categories")
def categories(
    db: Session = Depends(get_db)
):
    return get_category_breakdown(db)


@router.get("/monthly")
def monthly(
    db: Session = Depends(get_db)
):
    return get_monthly_spend(db)