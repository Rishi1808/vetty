from fastapi import APIRouter, Depends, Query
from app.services.coingecko import fetch_coins, fetch_coin_details
from app.services.pagination import paginate
from app.core.security import verify_api_key

router = APIRouter()

@router.get("/coins", dependencies=[Depends(verify_api_key)])
async def list_coins(page_num: int = Query(1, ge=1), per_page: int = Query(10, ge=1)):
    coins = fetch_coins()
    return paginate(coins, page_num, per_page)

@router.get("/coins/{coin_id}", dependencies=[Depends(verify_api_key)])
async def get_coin(coin_id: str):
    return fetch_coin_details(coin_id, currency="cad")