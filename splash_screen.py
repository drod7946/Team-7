# splash_screen.py
import tkinter as tk
from PIL import Image, ImageTk
from entry_screen_final import show_entry_screen

def show_splash(root):
    splash = tk.Toplevel(root)
    splash.geometry("1600x900")
    splash.title("Splash Screen")
    splash.resizable(True, True)

    # Load the image
    image = Image.open("logo.jpg")
    image = image.resize((1600, 900))
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(splash, image=photo)
    label.image = photo 
    label.pack()
    
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
