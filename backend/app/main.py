from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import engine
from app.models.transaction import Transaction
from app.core.database import Base

from app.api.routes import router
from app.routes.upload import router as upload_router
from app.api.analytics import router as analytics_router

Base.metadata.create_all(bind=engine)

app = FastAPI( title = "Credit Card Recommendation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*",]
)

app.include_router(router)
app.include_router(upload_router)
app.include_router(analytics_router)