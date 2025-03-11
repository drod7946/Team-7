# splash_screen.py
import tkinter as tk
from PIL import Image, ImageTk
import entry_screen_final

def show_splash(root):
    splash = tk.Toplevel(root)
    splash.geometry("400x300")
    splash.title("Splash Screen")

    # Load the image
    image = Image.open("logo.jpg")
    image = image.resize((400, 300))
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(splash, image=photo)
    label.image = photo 
    label.pack()
    # Transition to the entry screen after 3 seconds
    splash.after(3000, show_entry_screen, root, splash)

    splash.protocol("WM_DELETE_WINDOW", splash.quit)

    splash.mainloop()

def show_entry_screen(root, splash):
    splash.destroy()  # Close splash screen
    entry_screen_final.show_entry_screen(root)  # Open entry screen

if __name__ == "__main__":
    root = tk.Tk()  # Create the root window
    root.withdraw()  # Hide the root window
    show_splash(root)