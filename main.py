import tkinter as tk
import splash_screen  # Import the splash screen functionality
from udp_utils import UDPReceiver, send_udp_message, get_target_ip

def handle_incoming_message(msg):
    send_udp_message('200', get_target_ip(), 7501)
    try:
        parts = msg.strip().split(":")
        if len(parts) != 2:
            print(f"Invalid message format: {msg}")
            return

        id1, id2 = parts

        if id2 in ["43", "53"]:  # special base hit codes
            print(f"Player {id1} hit base {id2}")
            # trigger base hit animation or update scoreboard
        else:
            print(f"Player {id1} hit {id2}")
            # trigger tag/interaction logic
    except Exception as e:
        print(f"Error handling message: {e}")


def main():
    receiver = UDPReceiver(callback=handle_incoming_message)
    receiver.start()

    root = tk.Tk()
    root.withdraw()  # Hide root window initially
    splash_screen.show_splash(root)  # Show the splash screen
    root.mainloop()  # Start main event loop

if __name__ == "__main__":
    main()
