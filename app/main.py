from fastapi import FastAPI
from app.routes import coins, categories  # Ensure this import is correct

app = FastAPI(
    title="Crypto Market API",
    description="Fetch cryptocurrency market updates.",
    version="1.0",
)

app.include_router(coins.router)
app.include_router(categories.router)
