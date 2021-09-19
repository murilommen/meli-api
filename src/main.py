import uvicorn
from fastapi import FastAPI

from app.routers import items
from app import models
from app.context_manager import engine


models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(items.router)


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
