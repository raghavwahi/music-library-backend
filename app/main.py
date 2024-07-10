"""
Main module for the FastAPI application.

This module initializes a FastAPI application and includes routes from the 'app.routes.songs' module.
It also configures logging and provides a root endpoint to check if the application is running.

Usage:
    Run this module to start the FastAPI application.
"""

import logging

from dotenv import load_dotenv
from fastapi import FastAPI

# Load environment variables from .env file
load_dotenv()

# Importing routes and initializing logging
from app.routes import songs
from app.util.logger import initialize_logging

# Initialize logging configuration
initialize_logging()

# Create FastAPI instance
app = FastAPI()

# Include the songs router
app.include_router(songs.router)


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
