from pydantic import BaseModel


class SummaryResponse(BaseModel):
    total_spend: float
    transaction_count: int
    average_monthly_spend: float


class CategoryResponse(BaseModel):
    category: str
    amount: float


class MonthlyResponse(BaseModel):
    month: str
    amount: float


class DashboardResponse(BaseModel):
    summary: SummaryResponse
    categories: list[CategoryResponse]
    monthly: list[MonthlyResponse]