import sys, os
import uvicorn
import mlflow

from fastapi import FastAPI
from config import settings
from model_loader import model
from api import router
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load Model
    mlflow.set_tracking_uri(settings.MLFLOW_URL)
    
    if settings.MODEL_DOWNLOAD_YN == "Y":
        model.download()
    model.load()
    print(f"Device Setting = {settings.DEVICE}")

    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8011)
    # uvicorn.run("main:app", host="0.0.0.0", port=8011, reload=True)