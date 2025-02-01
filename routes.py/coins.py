from fastapi import APIRouter
import requests
import os

API_KEY = os.getenv("API_KEY")  # Make sure the API key is set in your environment variables

router = APIRouter()

@router.get("/coins")
def get_coins():
    url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
    response = requests.get(url)
    data = response.json()
    return {"data": data}
