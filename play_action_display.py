import tkinter as tk
from PIL import Image, ImageTk
import os
import pygame
import threading
import time
from udp_utils import UDPReceiver, send_udp_message, get_target_ip
import random

pygame.mixer.init()
music_folder = "photon_tracks"

def choose_track(folder):
    tracks = [f for f in os.listdir(folder)]

    if not tracks:
        print('Error, no track found')
        return None

    return os.path.join(folder, random.choice(tracks))

def play_audio(file_path):
    time.sleep(17)
    if not os.path.exists(file_path):
        print('file not found')
        return

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

def start_audio():
    track = choose_track(music_folder)
    threading.Thread(target=play_audio, args=(track,), daemon=True).start()

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
    play_window.attributes('-fullscreen', True)
    play_window.bind("<Escape>", lambda event: play_window.attributes('-fullscreen', False))
    play_window.resizable(True, True)  
    play_window.configure(bg="black")

    canvas = tk.Canvas(play_window, width=1900, height=1000, bg="black", highlightthickness=0)
    canvas.pack(pady=20)

    canvas.create_text(950, 25, text="PLAY ACTION DISPLAY", font=("Helvetica", 24, "bold"), fill="white")

    # Red box (x1, y1, x2, y2)
    canvas.create_rectangle(0, 0, 600, 987, fill="red", outline="white", width=3)

    # Green box
    canvas.create_rectangle(1300, 0, 1900, 987, fill="green", outline="white", width=3)
	
    timer_text = canvas.create_text(950, 950, text="06:00", font=("Helvetica", 48, "bold"), fill="white")
    canvas.pack(pady=20)
    
    canvas.create_text(300, 50, text="Red Team", font=("Helvetica", 24, "bold"), fill="white")
    canvas.create_text(1600, 50, text="Green Team", font=("Helvetica", 24, "bold"), fill="white")

    red_team_members = ["Player 1", "Player 2", "Player 3"]
    for i, player in enumerate(red_team_members, start=1):
        canvas.create_text(300, 100 + (i * 40), text=player, font=("Helvetica", 16), fill="white")
    
    green_team_members = ["Player A", "Player B", "Player C"]
    for i, player in enumerate(green_team_members, start=1):
        canvas.create_text(1600, 100 + (i * 40), text=player, font=("Helvetica", 16), fill="white")

    action_box = tk.Text(play_window, width=50, height=10, wrap=tk.WORD, font=("Helvetica", 14), bg="black", fg="white")
    action_box.pack(pady=20)

    def handle_incoming_message(msg):
        try:
            parts = msg.strip().split(":")
            if len(parts) != 2:
                print(f"Invalid message format: {msg}")
                return

            id1, id2 = parts
            log_message = ""

            if id2 in ["43", "53"]:
                log_message = f"Player {id1} hit base {id2}"
            else:
                log_message = f"Player {id1} hit {id2}"

            print(log_message)
            action_box.insert(tk.END, log_message + "\n")
            action_box.see(tk.END)  # Auto-scroll

            send_udp_message('200', get_target_ip(), 7500)

        except Exception as e:
            error_msg = f"Error handling message: {e}"
            print(error_msg)
            action_box.insert(tk.END, error_msg + "\n")
            action_box.see(tk.END)
    receiver = UDPReceiver(callback=handle_incoming_message)
    receiver.start()
    
    send_udp_message("202", get_target_ip(), 7500)

    def update_timer(canvas, timer_text, time_left):
        minutes = time_left // 60
        seconds = time_left % 60
        canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
        
        if time_left > 0:
            canvas.after(1000, update_timer, canvas, timer_text, time_left - 1)
        else:
            for _ in range(3):
                send_udp_message("221", get_target_ip(), 7500)
                time.sleep(0.2)
            show_return(play_window)

    update_timer(canvas, timer_text, 360)

def show_countdown():
    start_audio()
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
