from fastapi import FastAPI
from app.routes import coins, categories  # Ensure this matches your directory structure

app = FastAPI(
    title="Crypto Market API",
    description="Fetch cryptocurrency market updates.",
    version="1.0",
)

# Make sure you're including the routers correctly
app.include_router(coins.router)
app.include_router(categories.router)
