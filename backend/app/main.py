from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from .config import get_settings
from . import routes


settings = get_settings()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Serve index.html
@app.get("/")
def read_index():
    return FileResponse("app/static/index.html")

@app.get('/info')
def get_info():
    return {
        "app_name": settings.APP_NAME,
        
    }

app.include_router(routes.router)