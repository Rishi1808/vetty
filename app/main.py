from fastapi import FastAPI
from app.api.v1.endpoints import coins, categories, health
from app.core.config import settings

app = FastAPI(title="Crypto Market API", version="1.0.0")

app.include_router(coins.router, prefix="/api/v1", tags=["coins"])
app.include_router(categories.router, prefix="/api/v1", tags=["categories"])
app.include_router(health.router, prefix="/api/v1", tags=["health"])