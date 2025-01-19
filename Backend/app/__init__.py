# This code was written by Andreas Mohr.
# Last change 16.01.2025.
# It initializes a FastAPI application, sets up CORS middleware, and includes API and WebSocket routes.

from fastapi import FastAPI
from app.routes import router as api_router
from app.websockets import websocket_routes
from fastapi.middleware.cors import CORSMiddleware

def create_app():
    app = FastAPI()

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allows requests from all origins (for development purposes)
        allow_credentials=True,
        allow_methods=["*"],  # Allows all HTTP methods (e.g., POST, GET)
        allow_headers=["*"],  # Allows all headers
    )

    # Include your routes here
    from app.routes import router as api_router
    app.include_router(api_router)

    # Register HTTP routes
    app.include_router(api_router)

    # Register WebSocket routes
    websocket_routes(app)

    return app