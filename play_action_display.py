import tkinter as tk
from PIL import Image, ImageTk
import os

def show_play_action_display(countdown_window):
    #Place play action display here
    #Something that adjusts countdown_window or you can have the destroy function first and 
    #create a new window with play_action_display = tk.Toplevel()
    
    countdown_window.destroy()

def show_countdown():
    countdown_window = tk.Toplevel()
    countdown_window.title("Game Starting In...")
    
    folder_path = "countdown_images"
    
    # Load the background
    background = Image.open(os.path.join(folder_path, "background.tif"))
    background_img = ImageTk.PhotoImage(background)

    # Create a Tkinter label for the display
    display_label = tk.Label(countdown_window, image=background_img)
    display_label.image = background_img  # Keep a reference to avoid garbage collection
    display_label.pack()

    # Countdown logic
    def update_countdown(i):
        if i >= 0:
            try:
                number_img = Image.open(os.path.join(folder_path, f"{i}.tif"))
                countdown_screen = background.copy()

                # Center the number image
                x_offset = 171
                y_offset = 204

                countdown_screen.paste(number_img, (x_offset, y_offset))
                countdown_img = ImageTk.PhotoImage(countdown_screen)

                display_label.configure(image=countdown_img)
                display_label.image = countdown_img  # Keep reference

                countdown_window.after(1000, update_countdown, i - 1)  # Delay 1 second for each step
            except FileNotFoundError:
                print(f"Number image {i}.tif not found. Skipping...")

        else:
            show_play_action_display(countdown_window)
            
    update_countdown(30)

    countdown_window.protocol("WM_DELETE_WINDOW", countdown_window.destroy)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Game")
    show_countdown(root)
    root.mainloop()
