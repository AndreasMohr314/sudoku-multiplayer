# This code was written by Andreas Mohr.
# Last change 16.01.2025.
# This module handles WebSocket connections for a multiplayer Sudoku game. It manages player sessions,
# real-time updates, and communication between players.

from fastapi import WebSocket, WebSocketDisconnect
from app.redis_client import get_session, update_session

# Active WebSocket connections
active_connections = {}

# Player status: tracks if both players are ready
session_players_ready = {}


def websocket_routes(app):
    @app.websocket("/ws/{session_id}")
    async def websocket_endpoint(websocket: WebSocket, session_id: str, player: str):
        await websocket.accept()

        # Initialize session-specific data if it does not exist
        if session_id not in active_connections:
            active_connections[session_id] = []
            session_players_ready[session_id] = {"player_1": False, "player_2": False}
        active_connections[session_id].append(websocket)

        print(f"New connection for session {session_id}. Active connections: {len(active_connections[session_id])}")

        # Load the saved session from Redis
        session_data = await get_session(session_id)
        if session_data:
            print(f"Session data found for {session_id}: {session_data}")
            # Send the saved Sudoku board to the client
            await websocket.send_json({"action": "init", "board_1": session_data["sudoku_1"], "board_2": session_data["sudoku_2"]})
        else:
            # If no session is found, send an empty board
            await websocket.send_json({"action": "init", "board_1": [[0] * 9 for _ in range(9)], "board_2": [[0] * 9 for _ in range(9)]})

        try:
            while True:
                # Receive data from the client
                data = await websocket.receive_json()

                if data.get("action") == "ready":
                    # Mark the player as ready
                    session_players_ready[session_id][f"player_{player}"] = True
                    print(f"Player {player} is ready.")

                    # Check if both players are ready
                    if all(session_players_ready[session_id].values()):
                        print(f"Game in session {session_id} is starting.")
                        for connection in active_connections[session_id]:
                            await connection.send_json({"action": "start"})

                elif data.get("action") == "input":
                    # Process user input
                    row = data.get("row")
                    col = data.get("col")
                    value = data.get("value")
                    player = data.get("player")

                    # Load the current session data
                    session_data = await get_session(session_id)
                    if session_data:
                        solution = session_data["solution"]
                        board_of_current_player = f"sudoku_{player}"

                        if value == solution[row][col]:
                            # The input is correct, update the board
                            session_data[board_of_current_player][row][col] = value
                            await update_session(session_id, session_data)

                            # Check if the Sudoku is completely solved
                            if session_data[board_of_current_player] == solution:
                                # Send a "Winner" message to all clients
                                for connection in active_connections[session_id]:
                                    await connection.send_json({"action": "winner", "player_win": player})
                            else:
                                # Send the updated board to all clients
                                for connection in active_connections[session_id]:
                                    await connection.send_json({"action": "update", "board_1": session_data["sudoku_1"], "board_2": session_data["sudoku_2"]})
                        else:
                            # The input is incorrect, send an error message to the user
                            for connection in active_connections[session_id]:
                                await connection.send_json({"action": "error", "message": "Incorrect number entered!", "row": row, "col": col, "error_player": player})
        except WebSocketDisconnect:
            active_connections[session_id].remove(websocket)
            print(f"WebSocket connection closed: {session_id}")
            if not active_connections[session_id]:
                del active_connections[session_id]

