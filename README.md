# Sudoku Multiplayer

A local multiplayer Sudoku game where players compete against each other within a network. Each player scans a QR code with their smartphone or follows a link on their PC to join the game and attempts to solve the Sudoku faster than their opponent. Designed for use in a home network.

Key Features:
- **Real-time Gameplay:** Players solve the Sudoku puzzle independently but compete against each other.
- **QR Code-based Login:** Quick and easy access to the game via QR codes.
- **Locally Hosted** Secure gameplay within a closed network.
## Demo
Here’s a quick look at the Sudoku game in action:

<video controls width="600" muted loop autoplay>
  <source src="./Frontend/public/videos/FullGame.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


## Installation

### Prerequisites
- **Python 3.8+**  
  [Download Python](https://www.python.org/downloads/)  
  Make sure to add Python to your PATH during installation.

- **Redis** (installed on your machine)  
  [Download Redis](https://redis.io/download)  
  For Windows, you can use the precompiled binaries from [Microsoft's GitHub](https://github.com/microsoftarchive/redis/releases).

- **Node.js** (with npm)  
  [Download Node.js](https://nodejs.org/)  
  The installation includes npm.

- **Git**  
  [Download Git](https://git-scm.com/downloads)  

---

### ⚠️ Firewall Configuration Warning

To ensure that smartphones can communicate with the server, you may need to create new firewall rules to allow traffic on the following ports:
- **Port 5000**: Used for the frontend and QR code generation.
- **Port 8000**: Used for the Python backend.

Make sure to:
1. **Allow traffic only from devices within the same network** to ensure security.
2. **Avoid exposing these ports to the internet** unless you have implemented additional security measures.

For guidance on setting up firewall rules, refer to:
- **Windows Firewall**: [Microsoft Support Guide](https://support.microsoft.com/en-us/windows/turn-microsoft-defender-firewall-on-or-off-0bde5f2e-bdb9-1a03-ecd6-ef6b7bcaf93b)  
- **Linux (UFW)**: [UFW Guide](https://help.ubuntu.com/community/UFW)  
- **Mac (PF)**: [Configuring the macOS PF Firewall](https://developer.apple.com/library/archive/documentation/Security/Conceptual/Security_Overview/BuildingaSecureNetwork/BuildingaSecureNetwork.html)

---

### Steps
1. **Clone the repository**:
    ```bash
    git clone https://github.com/username/sudoku-multiplayer.git
    cd sudoku-multiplayer
    ```

2. **Set up the backend**:
    ```bash
    cd Backend
    pip install -r requirements.txt
    ```

3. **Start Redis**:
    Make sure Redis is running:
    ```bash
    redis-server
    ```
    If you're new to Redis, check out this guide:  
    [Redis Quick Start](https://redis.io/docs/getting-started/)

4. **Set up the frontend**:
    ```bash
    cd ../Frontend
    npm install
    ```
5. **Set your local IP address in the code**:

Before starting the project, make sure to set your local IP address in the `localIP` variable in the `Frontend/src/routes/SudokuGame.svelte` file. This is necessary for the application to connect to the WebSocket server correctly.

#### Steps to set your local IP address:
1. Open the file `Frontend/src/routes/SudokuGame.svelte`.
2. Locate the following section in the code:
    ```javascript
    //----------------------------------------------------------
    // Configuration: Please set your local IP address below
    // Replace the placeholder with your local IP address
    // Example: const localIP = "192.168.0.100";
    //----------------------------------------------------------
    const localIP = ""; // Change this to your local IP address
    //----------------------------------------------------------
    ```
3. Replace "" with the local IP address of your machine.

#### How to find your local IP address:
- **Windows**:
  1. Open the Command Prompt and type `ipconfig`.
  2. Look for the line `IPv4 Address` under your active network connection.
- **Linux/Mac**:
  1. Open the terminal and type `ifconfig` or `ip a`.
  2. Find the `inet` address associated with your active network connection.

#### Example:
If your local IP address is `192.168.1.100`, update the variable as follows:
```javascript
const localIP = "192.168.1.100";
```

6. **Start the project**:
    - Backend:
        ```bash
        cd ../Backend
        python run.py
        ```
    - Frontend:
        ```bash
        cd ../Frontend
        npm run dev
        ```

7. **Open in the browser**:
    - Navigate to `http://<your-local-ip>:5000` (replace `<your-local-ip>` with your computer's IP address on the network).

8. **Use the provided script for simplified startup**:
    The project includes two scripts, one for Windows and one for Linux/Mac, to automate the server setup and launch process:
    
    - **Windows**: `start_servers_without_paths.cmd`  
    - **Linux/Mac**: `start_servers_without_paths.sh`
    
    Before running the scripts, you need to edit the files to set the paths to your server directories and your local IP address. Once configured, the scripts will:
    - Start the Redis server.
    - Start the Python backend server.
    - Start the frontend server.
    - Open a browser window pointing to the frontend (`http://<your-local-ip>:5000`).
    
    **Example usage**:  
    - Windows:
        ```cmd
        start_servers_without_paths.cmd
        ```
    - Linux/Mac:
        ```bash
        ./start_servers_without_paths.sh
        ```

---

### Additional Resources
- **How to set up Redis on Windows**: [Step-by-step guide](https://redis.io/docs/getting-started/installation/install-redis-on-windows/)  
- **Learn more about Node.js and npm**: [Node.js Documentation](https://nodejs.org/en/docs/)  
- **Git basics for beginners**: [Git Tutorial](https://git-scm.com/doc)  

## How to Play

1. **Scan QR Codes**:
    - Open the displayed webpage (`http://<your-local-ip>:5000`) on your PC.
    - Scan the QR code on the webpage with your smartphone to connect to the game.

2. **Multiplayer Mode**:
    - Two players connect with their smartphones.
    - Each player tries to solve the Sudoku puzzle faster than the other.

3. **Determine the Winner**:
    - The player who solves the Sudoku puzzle first wins.
    - In case of any issues, the game automatically updates to synchronize both devices.

## Technologies
- **Python**: Backend server and game logic.
- **Redis**: Temporary data storage during the game.
- **Svelte**: Frontend framework for the user interface.
- **Bootstrap**: Responsive design and styles.
- **QRCode**: Generation of QR codes for quick access.

## Folder Structure

```plaintext
sudoku-multiplayer/
│
├── Backend/              # Python backend with game logic
│   ├── app/              # Core game logic
│   ├── qr_codes/         # Temporary QR code images
│   └── run.py            # Entry point for the backend server
│
├── Frontend/             # Svelte frontend
│   ├── src/              # UI source code
│   ├── public/           # Static files
│   └── package.json      # npm dependencies
│
├── README.md             # Project description
├── .gitignore            # Git ignore file
├── start_servers_without_paths.cmd
└── start_servers_without_paths.sh
