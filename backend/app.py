"""Railway entry point - app.py is auto-detected."""

import os
import uvicorn

# Import the FastAPI app
from src.main import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("src.main:app", host="0.0.0.0", port=port)
