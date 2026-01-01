from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from .weather_api import get_weather_data
from .cache import get_data_from_cache, store_data_in_cache
from typing import Optional
import json
from .config import templates


router = APIRouter()


@router.get('/', response_class=HTMLResponse)
async def load_page(request: Request, context_dict: dict = dict()):
    return templates.TemplateResponse(
        request=request, name="index.html", context=context_dict
    )


@router.get('/get-weather-data')
def get_weather_data_api(location: str, start_date: Optional[str] = "", end_date: Optional[str] = ""):
    if not location:
        raise HTTPException(
            status_code=400,
            detail="location is required"
        )

    cached_data = get_data_from_cache(location, start_date, end_date)

    if cached_data:
        return cached_data

    api_response = get_weather_data(location, start_date, end_date)

    with open('response.json', 'w') as f:
        json.dump(api_response, f)

    cache_response = store_data_in_cache(location, start_date, end_date, api_response)

    return cache_response
