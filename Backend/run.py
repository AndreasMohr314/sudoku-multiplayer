# This code was written by Andreas Mohr.
# Last change 16.01.2025.
# This script starts the FastAPI application and serves static files for QR codes.

import uvicorn
from app import create_app
from fastapi.staticfiles import StaticFiles

# Create the FastAPI application instance
app = create_app()

# Mount the directory for serving static QR code files
app.mount("/qr_codes", StaticFiles(directory="qr_codes"), name="qr_codes")

if __name__ == "__main__":
    # Run the FastAPI application on host 0.0.0.0 and port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
