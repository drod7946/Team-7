import tkinter as tk
import splash_screen

if __name__ == "__main__":
    root = tk.Tk()  # Create the root window
    root.withdraw()  # Hide the root window
    splash_screen.show_splash(root)
