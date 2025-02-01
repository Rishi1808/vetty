import httpx

COINGECKO_URL = "https://api.coingecko.com/api/v3"

async def fetch_coins():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{COINGECKO_URL}/coins/list")
        return response.json()

async def fetch_coin_details(coin_id: str, currency: str = "cad"):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{COINGECKO_URL}/coins/{coin_id}",
            params={"localization": "false", "tickers": "false", "market_data": "true", "community_data": "false", "developer_data": "false", "sparkline": "false"}
        )
        return response.json()

async def fetch_categories():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{COINGECKO_URL}/coins/categories/list")
        return response.json()