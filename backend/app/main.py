from fastapi import FastAPI, HTTPException
from .config import get_settings
from . import routes


settings = get_settings()

app = FastAPI()


@app.get('/')
def read_root():
    return {
        "message": 'Hello World'
    }

@app.get('/info')
def get_info():
    return {
        "app_name": settings.APP_NAME,
        
    }

app.include_router(routes.router)