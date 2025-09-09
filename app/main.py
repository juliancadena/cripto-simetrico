from fastapi import FastAPI
from app.routers import aes

def create_app() -> FastAPI:
    app = FastAPI(title="AES API", description="API for AES encryption and decryption", version="0.1.0")

    app.include_router( aes.router, prefix="/aes", tags=["aes"] )

    return app

app = create_app()