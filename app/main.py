"""
Main module for the FastAPI application.

This module initializes a FastAPI application and includes routes from the 'app.routes.songs'
module.
It also configures logging and provides a root endpoint to check if the application is running.

Usage:
    Run this module to start the FastAPI application.
"""

import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables from .env file
load_dotenv()

# Importing routes and initializing logging
from app.routes import songs  # pylint: disable=wrong-import-position
from app.util.logger import initialize_logging  # pylint: disable=wrong-import-position

# Initialize logging configuration
initialize_logging()

# Create FastAPI instance
app = FastAPI()


# Include the songs router
app.include_router(songs.router)


def get_allowed_origins_from_env():
    allowed_origins_str = os.getenv("ALLOWED_ORIGINS", "").strip()
    allowed_origins = [origin.strip() for origin in allowed_origins_str.split(",") if origin.strip()]
    return allowed_origins


app.add_middleware(
    CORSMiddleware,
    allow_origins=get_allowed_origins_from_env(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    """
    Root endpoint of the FastAPI application.

    Returns:
        dict: A dictionary with a message indicating the application is up and running.
    """
    message = "Application is up and running."
    logging.info(message)

    return {"message": message}


if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI application using Uvicorn server
    uvicorn.run(app)
