import tkinter as tk
import splash_screen  # Import the splash screen functionality

def main():
    root = tk.Tk()
    root.withdraw()  # Hide root window initially
    splash_screen.show_splash(root)  # Show the splash screen
    root.mainloop()  # Start main event loop

if __name__ == "__main__":
    main()
