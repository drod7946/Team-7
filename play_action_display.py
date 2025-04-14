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
    time.sleep(15)
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
    window_width = 300
    window_height = 100
    screen_width = restart_window.winfo_screenwidth()
    screen_height = restart_window.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    restart_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    label = tk.Label(restart_window, text="Do you want to return to the entry screen?")
    label.pack(pady=10)

    button_frame = tk.Frame(restart_window)
    button_frame.pack()

    tk.Button(button_frame, text="Yes", width=10, command=on_yes).grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="No", width=10, command=on_no).grid(row=0, column=1, padx=10)
    restart_window.bind("<KeyPress-y>", lambda event: on_yes())
    restart_window.bind("<KeyPress-n>", lambda event: on_no())
    restart_window.protocol("WM_DELETE_WINDOW", restart_window.destroy)

def show_play_action_display(countdown_window, player_dict):
    countdown_window.destroy()
    play_window = tk.Toplevel()
    play_window.title("Play Action Display")
    play_window.attributes('-fullscreen', True)
    play_window.bind("<Escape>", lambda event: play_window.attributes('-fullscreen', False))
    play_window.resizable(True, True)
    play_window.configure(bg="black")

    canvas = tk.Canvas(play_window, bg="black", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    screen_width = play_window.winfo_screenwidth()
    screen_height = play_window.winfo_screenheight()
    third_width = screen_width // 3

    red_border = canvas.create_rectangle(0, 0, third_width, screen_height, fill="red", outline="white", width=3)
    center_border = canvas.create_rectangle(third_width, 0, 2 * third_width, screen_height, fill="black", outline="white", width=3)
    green_border = canvas.create_rectangle(2 * third_width, 0, screen_width, screen_height, fill="green", outline="white", width=3)

    canvas.create_text(screen_width // 2, 25, text="PLAY ACTION DISPLAY", font=("Helvetica", 24, "bold"), fill="white")
    timer_text = canvas.create_text(screen_width // 2, screen_height - 50, text="06:00", font=("Helvetica", 48, "bold"), fill="white")

    action_box = tk.Text(play_window, width=60, height=32, wrap=tk.WORD, font=("Helvetica", 14), bg="black", fg="white", relief="flat", bd=0)
    canvas.create_window(screen_width // 2, screen_height // 2, window=action_box)

    base_hit_players = set()
    player_scores = {pid: 0 for pid in player_dict}
    red_team_members = [pid for pid, p in player_dict.items() if p["team"] == "red"]
    green_team_members = [pid for pid, p in player_dict.items() if p["team"] == "green"]

    def draw_team_names():
        canvas.delete("team_labels")
        red_total = 0
        green_total = 0

        canvas.create_text(100, 50, text="Red Team Scores", font=("Helvetica", 18, "bold"), fill="white", anchor="w", tags="team_labels")
        sorted_red = sorted(red_team_members, key=lambda pid: player_scores[pid], reverse=True)
        for i, pid in enumerate(sorted_red, start=1):
            player = player_dict[pid]
            label = f"{player['name']} [B]" if pid in base_hit_players else player["name"]
            score = player_scores[pid]
            red_total += score
            canvas.create_text(100, 50 + i * 40, text=label, font=("Helvetica", 16), fill="white", anchor="w", tags="team_labels")
            canvas.create_text(300, 50 + i * 40, text=str(score), font=("Helvetica", 16), fill="white", anchor="e", tags="team_labels")

        canvas.create_text(100, 50 + (len(red_team_members) + 1) * 40, text=f"Total Score: {red_total}", font=("Helvetica", 16, "bold"), fill="white", anchor="w", tags="team_labels")

        canvas.create_text(1300, 50, text="Green Team Scores", font=("Helvetica", 18, "bold"), fill="white", anchor="w", tags="team_labels")
        sorted_green = sorted(green_team_members, key=lambda pid: player_scores[pid], reverse=True)
        for i, pid in enumerate(sorted_green, start=1):
            player = player_dict[pid]
            label = f"{player['name']} [B]" if pid in base_hit_players else player["name"]
            score = player_scores[pid]
            green_total += score
            canvas.create_text(1300, 50 + i * 40, text=label, font=("Helvetica", 16), fill="white", anchor="w", tags="team_labels")
            canvas.create_text(1500, 50 + i * 40, text=str(score), font=("Helvetica", 16), fill="white", anchor="e", tags="team_labels")

        canvas.create_text(1300, 50 + (len(green_team_members) + 1) * 40, text=f"Total Score: {green_total}", font=("Helvetica", 16, "bold"), fill="white", anchor="w", tags="team_labels")

    def blink_border(team_border, blink=True, count=0):
        if count >= 10:
            return
        new_color = "yellow" if blink else "white"
        canvas.itemconfig(team_border, outline=new_color)
        canvas.after(500, blink_border, team_border, not blink, count + 1)

    def update_team_highlight():
        red_score = sum(player_scores[pid] for pid in red_team_members)
        green_score = sum(player_scores[pid] for pid in green_team_members)
        if red_score > green_score:
            blink_border(red_border)
            canvas.itemconfig(green_border, outline="white")
        elif green_score > red_score:
            blink_border(green_border)
            canvas.itemconfig(red_border, outline="white")
        else:
            canvas.itemconfig(red_border, outline="white")
            canvas.itemconfig(green_border, outline="white")

    def process_message(msg):
        try:
            parts = msg.strip().split(":")
            if len(parts) != 2:
                print(f"Invalid message: {msg}")
                return
            id1, id2 = parts
            if id1 not in player_dict:
                return
            if id2 in ["43", "53"]:
                base_hit_players.add(id1)
                player_scores[id1] += 100
                base_name = "Red Base" if id2 == "43" else "Green Base"
                log = f"{player_dict[id1]['name']} hit {base_name} (+100)"
            else:
                player_scores[id1] += 10
                target_name = player_dict.get(id2, {}).get("name", f"ID {id2}")
                log = f"{player_dict[id1]['name']} hit {target_name} (+10)"

            draw_team_names()
            update_team_highlight()
            print(log)
            action_box.insert(tk.END, log + "\n")
            action_box.see(tk.END)
            send_udp_message("200", get_target_ip(), 7500)

        except Exception as e:
            action_box.insert(tk.END, f"Error: {e}\n")
            action_box.see(tk.END)

    def handle_incoming_message(msg):
        play_window.after(0, process_message, msg)

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

    draw_team_names()
    update_team_highlight()
    update_timer(canvas, timer_text, 360)

    receiver = UDPReceiver(callback=handle_incoming_message)
    receiver.start()
    send_udp_message("202", get_target_ip(), 7500)

def show_countdown(player_dict):
    start_audio()
    countdown_window = tk.Toplevel()
    countdown_window.title("Game Starting In...")
    folder_path = "countdown_images"

    background = Image.open(os.path.join(folder_path, "background.tif"))
    background_img = ImageTk.PhotoImage(background)
    display_label = tk.Label(countdown_window, image=background_img, anchor="center")
    display_label.image = background_img
    display_label.pack()

    def update_countdown(i):
        if i >= 0:
            try:
                number_img = Image.open(os.path.join(folder_path, f"{i}.tif"))
                countdown_screen = background.copy()
                countdown_screen.paste(number_img, (171, 204))
                screen_width = countdown_window.winfo_screenwidth()
                screen_height = countdown_window.winfo_screenheight()
                window_x = int(screen_width * 0.6)
                window_y = int(screen_height * 0.7)
                countdown_window.geometry(f"{window_x}x{window_y}+{(screen_width - window_x) // 2}+{(screen_height - window_y) // 2}")
                countdown_screen = countdown_screen.resize((window_x, window_y), Image.LANCZOS)
                countdown_img = ImageTk.PhotoImage(countdown_screen)
                display_label.configure(image=countdown_img)
                display_label.image = countdown_img
                countdown_window.after(1000, update_countdown, i - 1)
            except FileNotFoundError:
                print(f"Missing: {i}.tif")
        else:
            show_play_action_display(countdown_window, player_dict)

    update_countdown(30)
    countdown_window.protocol("WM_DELETE_WINDOW", countdown_window.destroy)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    show_countdown({})
    root.mainloop()
