# This code was written by Andreas Mohr.
# Last change 16.01.2025.
# It provides asynchronous functions to interact with a Redis database for saving, retrieving, and updating session data.

import json
from redis.asyncio import Redis

# Establish asynchronous Redis connection
redis_client = Redis(host="localhost", port=6379, decode_responses=True)

# Save the session data into Redis.
async def save_session(session_id, sudoku, solution):

    try:
        # Store the Sudoku data without "mapping"
        await redis_client.hset(session_id, "sudoku_1", json.dumps(sudoku))
        await redis_client.hset(session_id, "sudoku_2", json.dumps(sudoku))
        await redis_client.hset(session_id, "solution", json.dumps(solution))
        print(f"Session {session_id} successfully saved.")
    except Exception as e:
        print(f"Error saving session {session_id}: {e}")

# Retrieve session data from Redis.
async def get_session(session_id):

    try:
        # Asynchronously load session data from Redis
        session_data = await redis_client.hgetall(session_id)
        if session_data:
            return {
                "sudoku_1": json.loads(session_data.get("sudoku_1", "{}")),  # Convert JSON string to Python object
                "sudoku_2": json.loads(session_data.get("sudoku_2", "{}")),  # Convert JSON string to Python object
                "solution": json.loads(session_data.get("solution", "{}"))   # Convert JSON string to Python object
            }
        return None
    except Exception as e:
        print(f"Error retrieving session {session_id}: {e}")
        return None

# Update specific session data in Redis.
async def update_session(session_id, data):

    try:
        # Update Sudoku and solution data explicitly as individual key-value pairs
        if "sudoku_1" in data:
            await redis_client.hset(session_id, "sudoku_1", json.dumps(data["sudoku_1"]))
        if "sudoku_2" in data:
            await redis_client.hset(session_id, "sudoku_2", json.dumps(data["sudoku_2"]))
        if "solution" in data:
            await redis_client.hset(session_id, "solution", json.dumps(data["solution"]))
        print(f"Session {session_id} successfully updated.")
    except Exception as e:
        print(f"Error updating session {session_id}: {e}")