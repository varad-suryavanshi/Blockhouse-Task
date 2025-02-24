# app/main.py
import uvicorn
from fastapi import FastAPI

from .models import Base
from .database import engine
from .routers import orders

# Create the SQLite tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Orders API")

# Include the orders router
app.include_router(orders.router, prefix="/orders", tags=["orders"])

# Optional: A root endpoint to test quickly
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    # For local development: python app/main.py
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
