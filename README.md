# Music Library (Backend)

## Table of Contents

- [Music Library (Backend)](#music-library-backend)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Features](#features)
  - [Environment Variables](#environment-variables)
  - [Initialization](#initialization)
  - [Accessing Swagger](#accessing-swagger)
  - [Coding Guidelines](#coding-guidelines)
  - [Contact](#contact)

## Description

This is the backend app for music library that is built using FastAPI which provides a robust and scalable API service.

## Features

- It can log required information into files.
- It has a structured application Setup.
- It can be used in a containerized setup.

## Environment Variables
To run this application, you need to set the following environment variables:

- `APP_ENV`: The environment in which the app is running (e.g., `DEV`, `PROD`).
- `DATABASE_URL`: The URL of the database to connect to.
- `LOG_LEVEL`: The logging level (e.g., `DEBUG`, `INFO`, `WARNING`, `ERROR`). 

Example `.env` file:
```dotenv
APP_ENV=DEV
DATABASE_URL=sqlite:///./test.db
LOG_LEVEL=DEBUG
```

## Initialization
Follow these steps to initialize the application:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/raghavwahi/music-library-backend
    cd music-library-backend
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Upgrade pip and install dependencies:**
    ```sh
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

4. **Set up the environment variables:**
    Create a `.env` file in the root directory and add your environment variables as described above.

5. **Run the database migrations:**
    ```sh
    python initialize_db.py
    ```

6. **Start the FastAPI application:**
    ```sh
    uvicorn app.main:app --reload
    ```

## Accessing Swagger
FastAPI automatically generates interactive API documentation using Swagger. To access the Swagger UI, follow these steps:

1. Start the FastAPI application using the initialization steps above.
2. Open your web browser and go to `http://127.0.0.1:8000/docs`.

Here, you can explore the API endpoints, send test requests, and see the API responses.

## Coding Guidelines
To maintain code quality and consistency, please follow these guidelines:

1. **Follow PEP 8:** Ensure that your code follows the PEP 8 style guide.
2. **Write Docstrings:** Document all functions and classes with appropriate docstrings.
3. **Type Annotations:** Use type annotations for function arguments and return values.
4. **Linting:** Use a linter (e.g., black, isort) to check your code for style issues before committing.
5. **Testing:** Write unit tests for your code and ensure that they pass before pushing changes.
6. **Commit Messages:** Use clear and concise commit messages. Follow the convention of starting with a capital letter.

## Contact

Raghav Wahi - [raghavwahi7@gmail.com](mailto:raghavwahi7@gmail.com)