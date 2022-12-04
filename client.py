import tkinter as tk
from tkinter import filedialog
import socket
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver
host = "10.49.66.109"
port = 5500

# create the client socket
s = socket.socket()

# Create the GUI window
window = tk.Tk()

def connect():
    # Display a label that shows we are connecting
    status_text = tk.Label(window, text=f"[+] Connecting to {host}:{port}")
    status_text.pack()

    # connect to the server
    s.connect((host, port))
    
    # Display a label that shows that we are connected
    status_text = tk.Label(window, text="[+] Connected.")
    status_text.pack()
    

# Define a function for transferring a file
def transfer_file():

    # Open a file dialog to select the file to transfer
    filename = filedialog.askopenfilename()
    
    filesize = os.path.getsize(filename)

    # Check if a file was selected
    if filename:
        # Send the file name and size
        s.send(f"{filename}{SEPARATOR}{filesize}".encode())
        # Get the file data
        with open(filename, "rb") as f:
            
            while True:
                # read the bytes from the file
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    # file transmitting is done
                    break
                
                s.sendall(bytes_read)

        # Transfer the file data to the specified location or device
        # ...

# Add a button to connect to the server
connection = tk.Button(window, text="Connect", command=connect)
connection.pack()

# Add a button to the GUI to trigger the file transfer
button = tk.Button(window, text="Transfer File", command=transfer_file)
button.pack()

# Run the GUI
window.mainloop()
