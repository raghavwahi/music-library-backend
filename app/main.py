import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

from app.routes import songs
from app.util.logger import initialize_logging

initialize_logging()
app = FastAPI()
app.include_router(songs.router)


@app.get("/")
def root():
    message = "Application is up and running."
    logging.info(message)

    return {"message": message}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
