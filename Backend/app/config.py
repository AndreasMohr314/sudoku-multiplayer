# This code was written by Andreas Mohr.
# Last change 16.01.2025.
# It defines a configuration class for storing application settings such as Redis and application ports.

class Config:
    REDIS_HOST = "localhost"  # The hostname for the Redis server
    REDIS_PORT = 6379          # The port number for the Redis server
    APP_PORT = 8000            # The port number for the application