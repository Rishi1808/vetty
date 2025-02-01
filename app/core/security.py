from fastapi import HTTPException, Depends, Header

API_KEY = "your-secure-api-key"

async def verify_api_key(api_key: str = Header(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")