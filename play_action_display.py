import tkinter as tk
from PIL import Image, ImageTk
import os
from udp_utils import send_udp_message, get_target_ip
import time

def show_return(play_window):
    def on_yes():
        restart_window.destroy()
        play_window.destroy()

    def on_no():
        restart_window.destroy()

    restart_window = tk.Toplevel()
    restart_window.title("Exit Game?")

    window_width = 250
    window_height= 100

    screen_width = restart_window.winfo_screenwidth()
    screen_height = restart_window.winfo_screenheight()

    # Calculate position x, y to center the window
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    restart_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    label = tk.Label(restart_window, text="Do you want to return to the entry screen?")
    label.pack(pady=10)

    button_frame = tk.Frame(restart_window)
    button_frame.pack()

    yes_button = tk.Button(button_frame, text="Yes", width=10, command=on_yes)
    yes_button.grid(row=0, column=0, padx=10)

    no_button = tk.Button(button_frame, text="No", width=10, command=on_no)
    no_button.grid(row=0, column=1, padx=10)

    # Bind 'y' and 'n' keys
    restart_window.bind("<KeyPress-y>", lambda event: on_yes())
    restart_window.bind("<KeyPress-n>", lambda event: on_no())

    restart_window.protocol("WM_DELETE_WINDOW", restart_window.destroy)
    

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
    
    # Add a label for the countdown timer
    timer_label = tk.Label(play_window, font=("Helvetica", 48, "bold"), fg="white", bg="black")
    timer_label.pack(pady=50)

    def update_timer(label, time_left):
        # Update the timer label with the time left
        minutes = time_left // 60
        seconds = time_left % 60
        label.config(text=f"{minutes:02}:{seconds:02}")
        
        # If time is not up, continue updating
        if time_left > 0:
            label.after(1000, update_timer, label, time_left - 1)  # Update every second
        else:
            for _ in range(3):
                send_udp_message("221", get_target_ip(), 7500)
                time.sleep(0.2)
            show_return(play_window)

    # Set initial time for 6:00 (360 seconds)
    update_timer(timer_label, 360)

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
            send_udp_message("202", get_target_ip(), 7500)
            
    update_countdown(30)

    countdown_window.protocol("WM_DELETE_WINDOW", countdown_window.destroy)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw() 
    show_countdown()
    root.mainloop()
