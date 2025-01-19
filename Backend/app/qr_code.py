# This code was written by Andreas Mohr.
# Last change 16.01.2025.
# It generates QR codes for two players based on a session ID and stores them in a designated folder.

import os
import qrcode
import socket  # This module is used for the get_local_ip function

# Retrieves the local IP address of your computer.
def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

# Generates two QR codes based on the session ID and saves them to the file system.
def generate_qr_code(session_id):
    local_ip = get_local_ip()
    url_1 = f"http://{local_ip}:5000/sudoku-game?session_id={session_id}&player=1"
    url_2 = f"http://{local_ip}:5000/sudoku-game?session_id={session_id}&player=2"

    # Generate QR code for player 1
    qr_1 = qrcode.QRCode(version=1, box_size=10, border=5)
    qr_1.add_data(url_1)
    qr_1.make(fit=True)
    img_1 = qr_1.make_image(fill="black", back_color="white")

    # Generate QR code for player 2
    qr_2 = qrcode.QRCode(version=1, box_size=10, border=5)
    qr_2.add_data(url_2)
    qr_2.make(fit=True)
    img_2 = qr_2.make_image(fill="black", back_color="white")

    # Create folder for QR codes if it doesn't exist
    qr_codes_folder = "qr_codes"
    if not os.path.exists(qr_codes_folder):
        os.makedirs(qr_codes_folder)

    # Path to player 1's QR code file
    file_name_1 = f"{session_id}_player1.png"
    path_1 = os.path.join(qr_codes_folder, file_name_1)

    # Path to player 2's QR code file
    file_name_2 = f"{session_id}_player2.png"
    path_2 = os.path.join(qr_codes_folder, file_name_2)

    # Save QR codes
    img_1.save(path_1)
    img_2.save(path_2)

    # Return URLs to the QR codes (frontend-compatible)
    return [f"/qr_codes/{file_name_1}", f"/qr_codes/{file_name_2}"]