import tkinter as tk
from PIL import Image, ImageTk
import os

def show_play_action_display(countdown_window):
    #Place play action display here
    #Something that adjusts countdown_window or you can have the destroy function first and 
    #create a new window with play_action_display = tk.Toplevel()
    
    countdown_window.destroy()
    play_window = tk.Toplevel()
    play_window.title("Play Action Display")
    play_window.geometry("1600x900") 
    play_window.resizable(True, True)  
    play_window.configure(bg="black")

    tk.Label(play_window, text="PLAY ACTION DISPLAY", font=("Helvetica", 24, "bold"), fg="white").pack(pady=20)

    team_frame = tk.Frame(play_window, bg="black")
    team_frame.pack(pady=20)

    team_frame.columnconfigure(0, weight=1)
    team_frame.columnconfigure(1, weight=1)

    red_team = tk.Label(team_frame, text="Red Team", font=("Helvetica", 20, "bold"), fg="red")
    red_team.grid(row=0, column=0, padx=50, pady=10)

    green_team = tk.Label(team_frame, text="Green Team", font=("Helvetica", 20, "bold"), fg="green")
    green_team.grid(row=0, column=1, padx=50, pady=10)

    red_team_members = ["Player 1", "Player 2", "Player 3"]
    for i, player in enumerate(red_team_members, start=1):
        tk.Label(team_frame, text=player, font=("Helvetica", 16), fg="white").grid(row=i, column=0, padx=50, pady=5)

    green_team_members = ["Player A", "Player B", "Player C"]
    for i, player in enumerate(green_team_members, start=1):
        tk.Label(team_frame, text=player, font=("Helvetica", 16), fg="white").grid(row=i, column=1, padx=50, pady=5)
    

def show_countdown():
    countdown_window = tk.Toplevel()
    countdown_window.title("Game Starting In...")
    
    folder_path = "countdown_images"
    
    # Load the background
    background = Image.open(os.path.join(folder_path, "background.tif"))
    background_img = ImageTk.PhotoImage(background)

    # Create a Tkinter label for the display
    display_label = tk.Label(countdown_window, image=background_img, anchor="center")
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
                
                # Now resize the entire combined image to the desired window size
                screen_width = countdown_window.winfo_screenwidth()
                screen_height = countdown_window.winfo_screenheight()

                # Example: scale to 60% width and 70% height
                window_x = int(screen_width * 0.6)
                window_y = int(screen_height * 0.7)

                countdown_window.geometry(f"{window_x}x{window_y}+{(screen_width - window_x) // 2}+{(screen_height - window_y) // 2}")

                countdown_screen = countdown_screen.resize((window_x, window_y), Image.LANCZOS)
                
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
    root.withdraw() 
    show_countdown()
    root.mainloop()
