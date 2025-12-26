from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from .weather_api import get_weather_data
from .cache import get_data_from_cache, store_data_in_cache
from typing import Optional
from .config import templates


router = APIRouter()


@router.get('/', response_class=HTMLResponse)
async def load_page(request: Request, context_dict: dict = dict()):
    return templates.TemplateResponse(
        request=request, name="index.html", context=context_dict
    )


@router.get('/get-weather-data')
def get_weather_data_api(location: str, start_date: Optional[str] = "", end_date: Optional[str] = ""):

    cached_data = get_data_from_cache(location, start_date, end_date)

    if cached_data:
        return cached_data

    api_response = get_weather_data(location, start_date, end_date)

    cache_response = store_data_in_cache(location, start_date, end_date, api_response)

    return cache_response
