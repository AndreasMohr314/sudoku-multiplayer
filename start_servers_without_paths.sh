#!/bin/bash

# Ensure the script is run as root (or with sudo)
if [ "$EUID" -ne 0 ]; then
  echo "This script must be run as root or with sudo."
  exit 1
fi

# Start Redis server
# Replace <REDIS_PATH> with the path to the folder where Redis is installed.
# Example: /usr/local/bin or /path/to/redis
echo "Starting Redis server..."
(cd <REDIS_PATH> && ./redis-server redis.conf) &

# Start Python server
# Replace <PYTHON_SERVER_PATH> with the path to the folder containing your Python server.
# Example: /home/username/project/backend
echo "Starting Python server..."
(cd <PYTHON_SERVER_PATH> && python3 run.py) &

# Start Frontend
# Replace <FRONTEND_PATH> with the path to the folder containing your frontend project.
# Example: /home/username/project/frontend
echo "Starting Frontend..."
(cd <FRONTEND_PATH> && npm run dev) &

# Wait for 6 seconds to ensure the Frontend server has started
echo "Waiting for 6 seconds to ensure the Frontend server is running..."
sleep 6

# Open the browser with the frontend URL
FRONTEND_URL="http://your-server-ip:your-port/"
echo "Opening browser to $FRONTEND_URL..."
xdg-open "$FRONTEND_URL" &

# Wait for user input to stop all processes
echo "All servers have been started. Press any key to stop all processes."
read -n 1 -s

# Stop all processes
echo "Stopping all processes..."

# Kill Redis server
echo "Stopping Redis server..."
pkill -f redis-server

# Delete all PNG files in the qr_codes folder before stopping the Python server
# Replace <QR_CODES_PATH> with the path to the qr_codes folder.
# Example: /home/username/project/backend/qr_codes
echo "Deleting PNG files in qr_codes folder..."
rm -f <QR_CODES_PATH>/*.png

# Kill Python server
echo "Stopping Python server..."
pkill -f "python3 run.py"

# Kill Frontend server (Node.js process)
echo "Stopping Frontend..."
pkill -f "npm run dev"

echo "All processes have been stopped."
