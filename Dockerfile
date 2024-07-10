# Use Python 3.12.3 as base image
FROM python:3.12.3

# Set environment variables
ENV APP_ENV=DEV
ENV DATABASE_URL=sqlite:///./test.db
ENV LOG_LEVEL=DEBUG

# Set working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Run database migrations
RUN python app/scripts/initialize_db.py

# Expose FastAPI port
EXPOSE 8000

# Command to run the FastAPI application with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
