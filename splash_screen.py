# splash_screen.py
import tkinter as tk
from PIL import Image, ImageTk
from entry_screen_final import show_entry_screen

def show_splash(root):
    splash = tk.Toplevel(root)
    splash.title("Splash Screen")
    splash.resizable(True, True)

    screen_x = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    available_height = splash.winfo_vrootheight()

    if available_height < screen_height:
        screen_y = available_height
    else:
        screen_y =screen_height

    window_x = int(screen_x)
    window_y = int(screen_y)

    center_x = (screen_x - window_x) // 2
    center_y = (screen_y - window_y) // 2

    splash.geometry(f"{window_x}x{window_y}+{center_x}+{center_y}")

    # Load the image
    image = Image.open("logo.jpg")
    image = image.resize((window_x, window_y), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(splash, image=photo)
    label.image = photo 
    label.pack(fill="both", expand=True)
    
    # Transition to the entry screen after 3 seconds
    splash.after(3000, start_entry_screen, root, splash)

    splash.protocol("WM_DELETE_WINDOW", splash.quit)

    splash.mainloop()

def start_entry_screen(root, splash):
    splash.destroy()  # Close splash screen
    show_entry_screen(root)  # Open entry screen

if __name__ == "__main__":
    root = tk.Tk()  # Create the root window
    root.withdraw()  # Hide the root window
    show_splash(root)
