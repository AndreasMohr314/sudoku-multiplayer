# This code was written by Andreas Mohr.
# Last change 16.01.2025.
# It defines API routes for creating Sudoku game sessions of varying difficulty levels and generating QR codes for them.

from fastapi import APIRouter
from app.qr_code import generate_qr_code
from app.sudoku_generator import generate_sudoku
from app.redis_client import save_session

router = APIRouter()

# Create a new easy Sudoku session.
@router.post("/create-easy-session")
async def create_session():

    # Generate a Sudoku board and its solution
    sudoku, solution = generate_sudoku(0.2)

    # Dynamically generate a session ID (e.g., UUID)
    import uuid
    session_id = f"sudoku_{uuid.uuid4().hex[:8]}"

    # Save the session in Redis
    await save_session(session_id, sudoku, solution)

    # Generate a QR code with the session ID
    qr_code_path = generate_qr_code(session_id)

    return {
        "session_id": session_id,
        "qr_code": qr_code_path
    }

# Create a new normal Sudoku session.
@router.post("/create-normal-session")
async def create_session():

    # Generate a Sudoku board and its solution
    sudoku, solution = generate_sudoku(0.5)

    # Dynamically generate a session ID (e.g., UUID)
    import uuid
    session_id = f"sudoku_{uuid.uuid4().hex[:8]}"

    # Save the session in Redis
    await save_session(session_id, sudoku, solution)

    # Generate a QR code with the session ID
    qr_code_path = generate_qr_code(session_id)

    return {
        "session_id": session_id,
        "qr_code": qr_code_path
    }

# Create a new difficult Sudoku session.
@router.post("/create-difficult-session")
async def create_session():

    # Generate a Sudoku board and its solution
    sudoku, solution = generate_sudoku(0.8)

    # Dynamically generate a session ID (e.g., UUID)
    import uuid
    session_id = f"sudoku_{uuid.uuid4().hex[:8]}"

    # Save the session in Redis
    await save_session(session_id, sudoku, solution)

    # Generate a QR code with the session ID
    qr_code_path = generate_qr_code(session_id)

    return {
        "session_id": session_id,
        "qr_code": qr_code_path
    }
