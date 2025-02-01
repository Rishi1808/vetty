from fastapi import APIRouter

router = APIRouter()

@router.get("/categories")
def get_categories():
    categories = ["Bitcoin", "Ethereum", "Litecoin"]
    return {"categories": categories}
