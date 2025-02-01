from typing import List, Dict

def paginate(data: List[Dict], page_num: int, per_page: int) -> Dict:
    start = (page_num - 1) * per_page
    end = start + per_page
    return {
        "page": page_num,
        "per_page": per_page,
        "total": len(data),
        "data": data[start:end]
    }