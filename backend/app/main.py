from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import engine
from app.models.transaction import Transaction
from app.models.credit_card import CreditCard
from app.core.database import Base

from app.routes.routes import router
from app.routes.upload import router as upload_router
from app.routes.analytics import router as analytics_router
from app.routes.test_recommendation import router as test_recommendation_router
from app.routes.recommendation import router as recommendation_router 
from app.routes.langchain_test import router as langchain_router
from app.routes.chat import router as chat_router

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
app.include_router(test_recommendation_router)
app.include_router(recommendation_router)
app.include_router(langchain_router)
app.include_router(chat_router)