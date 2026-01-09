from fastapi import FastAPI

app = FastAPI(title="Secure Backend API")


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


