from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Application is up and running."}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
