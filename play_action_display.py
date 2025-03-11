import tkinter as tk
from PIL import Image, ImageTk
import os
import time

# def show_play_action_display(root):
#     show_countdown(root)


# def show_countdown(root):
#     folder_path = "countdown_images"

#     background = Image.open(os.path.join(folder_path, "background.tif"))
#     background_img = ImageTk.PhotoImage(background)

#     display_label = tk.Label(root, image=background_img)
#     display_label.image = background_img  # Keep a reference to avoid garbage collection
#     display_label.pack()

#     # Countdown sequence (e.g., 5 to 1)
#     for i in range(30, -1, -1):
#         # Load the number image
#         number_img = Image.open(os.path.join(folder_path, f"{i}.tif"))
#         countdown_screen = background.copy()

#         # Calculate position to center the number image
#         x_offset = (background.width - number_img.width) // 2
#         y_offset = (background.height - number_img.height) // 2

#         # Create a copy of the background to avoid modifying the original
#         countdown_screen.paste(number_img, (x_offset, y_offset), mask=None)
#         countdown_img = ImageTk.PhotoImage(countdown_screen)

#         display_label.configure(image=countdown_img)
#         display_label.image = countdown_img
#         countdown_img.pack()
        
#         time.sleep(1)  # Pause for 1 second

# if __name__ == "__main__":
#     root = tk.Tk()  # Create the root window
#     root.withdraw()  # Hide the root window
#     show_countdown(root)

def show_play_action_display(root):
    show_countdown(root)

def show_countdown(root):
    folder_path = "countdown_images"
    
    # Load the background
    background = Image.open(os.path.join(folder_path, "background.tif"))
    background_img = ImageTk.PhotoImage(background)

    # Create a Tkinter label for the display
    display_label = tk.Label(root, image=background_img)
    display_label.image = background_img  # Keep a reference to avoid garbage collection
    display_label.pack()

    # Countdown logic
    def update_countdown(i):
        if i >= 0:
            try:
                number_img = Image.open(os.path.join(folder_path, f"{i}.tif"))
                countdown_screen = background.copy()

                # Center the number image
                x_offset = (background.width - number_img.width) // 2
                y_offset = (background.height - number_img.height) // 2

                countdown_screen.paste(number_img, (x_offset, y_offset))
                countdown_img = ImageTk.PhotoImage(countdown_screen)

                display_label.configure(image=countdown_img)
                display_label.image = countdown_img  # Keep reference

                root.after(1000, update_countdown, i - 1)  # Delay 1 second for each step
            except FileNotFoundError:
                print(f"Number image {i}.tif not found. Skipping...")

    update_countdown(30)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")  # Adjust size as needed
    show_countdown(root)
    root.mainloop()