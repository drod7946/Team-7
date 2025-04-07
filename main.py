import tkinter as tk
import splash_screen  # Import the splash screen functionality
from udp_utils import UDPReceiver

def handle_incoming_message(msg):
    print(f"[RECEIVED] {msg}")
    # TODO: Parse and update game state / UI 

def main():
    receiver = UDPReceiver(callback=handle_incoming_message)
    receiver.start()

    root = tk.Tk()
    root.withdraw()  # Hide root window initially
    splash_screen.show_splash(root)  # Show the splash screen
    root.mainloop()  # Start main event loop

if __name__ == "__main__":
    main()
