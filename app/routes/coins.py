from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("/coins")
def get_coins():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
    response = requests.get(url)
    data = response.json()

    # Return the data correctly
    return {"data": data}
