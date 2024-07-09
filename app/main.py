from dotenv import load_dotenv
from fastapi import FastAPI

from app.util.logger import initialize_logging
import logging

load_dotenv()
initialize_logging()
app = FastAPI()


@app.get("/")
def root():
    message = "Application is up and running."
    logging.info(message)

    return {"message": message}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
