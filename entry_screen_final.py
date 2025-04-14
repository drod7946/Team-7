from tkinter import *
import customtkinter
import tkinter as tk
import psycopg2
from play_action_display import show_countdown
from udp_utils import set_target_ip, get_target_ip
from tkinter import simpledialog, messagebox

def connect_to_db():
    try:
        connection = psycopg2.connect("dbname=photon user=student password=student host=localhost port=5432")
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

# Function to insert player equipment ID into database
def insert_player(player_id, codename):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO players (id, codename) VALUES (%s, %s);", (player_id, codename))
            connection.commit()
            print(f"Inserted Player ID: {player_id}, Codename: {codename}")
        except Exception as e:
            print(f"Error inserting player: {e}")
        finally:
            cursor.close()
            connection.close()

def get_player_codename(player_id):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT codename FROM players WHERE id = %s;", (player_id,))
            result = cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Error fetching player: {e}")
            return None
        finally:
            cursor.close()
            connection.close()

# ENTRY SCREEN UI

def show_entry_screen(root):
    customtkinter.set_appearance_mode("dark")
    entry_screen_window = customtkinter.CTkToplevel(root)
    entry_screen_window.title("Entry Terminal")

    screen_width = entry_screen_window.winfo_screenwidth()
    screen_height = entry_screen_window.winfo_screenheight()
    center_x = int(screen_width / 2 - 1350 / 2)
    center_y = int(screen_height / 2 - 900 / 2)
    entry_screen_window.geometry(f"1350x900+{center_x}+{center_y}")
    entry_screen_window.update()

    entry_fields = []
    player_dict = {}

    def handle_player_entry():
        for entry1, entry2, team in entry_fields:
            player_id = entry1.get().strip()
            codename = entry2.get().strip()

            if not player_id or player_id in player_dict:
                continue
            if not player_id.isdigit():
                messagebox.showerror("Invalid Player ID", f"Player ID must be an integer. Invalid input: '{player_id}'")
                continue

            db_name = get_player_codename(player_id)
            if db_name:
                codename = db_name
            elif not codename:
                codename = simpledialog.askstring("New Player", f"Enter codename for new player ID: {player_id}")
                if not codename:
                    continue
                insert_player(player_id, codename)
            else:
                insert_player(player_id, codename)

            entry2.config(state="normal")
            entry2.delete(0, tk.END)
            entry2.insert(0, codename)
            entry2.config(state="readonly")
            player_dict[player_id] = {"name": codename, "team": team}

    def manual_insert():
        player_id = simpledialog.askstring("Manual Insert", "Enter Player ID:")
        if not player_id:
            return
        codename = simpledialog.askstring("Manual Insert", f"Enter codename for Player {player_id}:")
        if not codename:
            return

        team = "red" if len([p for p in player_dict.values() if p['team'] == 'red']) < 16 else "green"

        if get_player_codename(player_id) is None:
            insert_player(player_id, codename)

        player_dict[player_id] = {"name": codename, "team": team}

        for entry1, entry2, t in entry_fields:
            if entry1.get().strip() == "":
                entry1.insert(0, player_id)
                entry2.config(state="normal")
                entry2.insert(0, codename)
                entry2.config(state="readonly")
                break

    def clear_entries():
        for entry1, entry2, _ in entry_fields:
            entry1.delete(0, tk.END)
            entry2.config(state="normal")
            entry2.delete(0, tk.END)
            entry2.config(state="readonly")
        player_dict.clear()

    def change_ip_popup():
        current_ip = get_target_ip()
        new_ip = simpledialog.askstring("Set Target IP", f"Current IP: {current_ip}\nEnter new target IP address:")
        if new_ip:
            parts = new_ip.strip().split(".")
            if len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts):
                set_target_ip(new_ip.strip())
                messagebox.showinfo("IP Address Set", f"New IP Address: {new_ip.strip()}")
            else:
                messagebox.showerror("Invalid IP", "Please enter a valid IPv4 address.")

    def on_button_click(text):
        print(f"Button {text} clicked")
        if text == "F5\nPreEntered\nGames":
            handle_player_entry()
            show_countdown(player_dict)
        elif text == "F12\nClear\nGame":
            clear_entries()
        elif text == "F7\nChange\nIP Address":
            change_ip_popup()

    def on_key_pressed(event):
        if event.keysym == "Return":
            print("Enter pressed")
            handle_player_entry()
        elif event.keysym == "Insert":
            print("Insert pressed")
            manual_insert()
        elif event.keysym == "F1": print("F1 pressed")
        elif event.keysym == "F2": print("F2 pressed")
        elif event.keysym == "F3": print("F3 pressed")
        elif event.keysym == "F5":
            print("F5 pressed")
            handle_player_entry()
            show_countdown(player_dict)
        elif event.keysym == "F7":
            print("F7 pressed")
            change_ip_popup()
        elif event.keysym == "F8": print("F8 pressed")
        elif event.keysym == "F10": print("F10 pressed")
        elif event.keysym == "F12":
            print("F12 pressed")
            clear_entries()

    entry_screen_window.bind("<Return>", on_key_pressed)
    entry_screen_window.bind_all("<F1>", on_key_pressed)
    entry_screen_window.bind_all("<F2>", on_key_pressed)
    entry_screen_window.bind_all("<F3>", on_key_pressed)
    entry_screen_window.bind_all("<F5>", on_key_pressed)
    entry_screen_window.bind_all("<F7>", on_key_pressed)
    entry_screen_window.bind_all("<F8>", on_key_pressed)
    entry_screen_window.bind_all("<F10>", on_key_pressed)
    entry_screen_window.bind_all("<F12>", on_key_pressed)
    entry_screen_window.bind_all("<Insert>", on_key_pressed)

    label = customtkinter.CTkLabel(entry_screen_window, text="Edit Current Game", font=("Helvetica", 18, "bold"), text_color="#99AAFF")
    label.pack(pady=0)

    frame = Frame(entry_screen_window)
    frame.pack(fill="both", expand=True, anchor="n")

    canvas = Canvas(frame, width=1350, height=900, bg=entry_screen_window.cget("bg"), highlightthickness=0)
    canvas.pack(fill="both", expand=True, anchor="n")

    canvas.create_rectangle(40, 10, 640, 600, fill="#B30000", outline="#B30000")
    canvas.create_rectangle(240, 20, 440, 60, outline="#DCDDDE")
    canvas.create_text(340, 40, text="RED TEAM", font=("Helvetica", 14), fill="#DCDDDE")

    canvas.create_rectangle(710, 10, 1310, 600, fill="#008000", outline="#008000")
    canvas.create_rectangle(910, 20, 1110, 60, outline="#DCDDDE")
    canvas.create_text(1010, 40, text="GREEN TEAM", font=("Helvetica", 14), fill="#DCDDDE")

    canvas.create_rectangle(445, 600, 905, 635, fill="#808A87", outline="#808A87")
    canvas.create_text(675, 617, text="Game Mode: Standard public mode", font=("Helvetica", 14, "bold"), fill="#DCDDDE")

    def create_input_fields(start_x, start_y, team):
        for i in range(16):
            y_offset = start_y + (i * 30)
            canvas.create_rectangle(start_x, y_offset, start_x + 17, y_offset + 17, outline="#DCDDDE")
            canvas.create_text(start_x + 35, y_offset + 8, text=str(i), font=("Helvetica", 14), fill="#DCDDDE")
            entry1 = Entry(entry_screen_window, font=("Helvetica", 14), bg="#DCDDDE", width=25)
            entry2 = Entry(entry_screen_window, font=("Helvetica", 14), bg="#DCDDDE", width=25, state="readonly")
            canvas.create_window(start_x + 50, y_offset + 8, window=entry1, anchor=W)
            canvas.create_window(start_x + 250, y_offset + 8, window=entry2, anchor=W)
            entry_fields.append((entry1, entry2, team))

    create_input_fields(50, 88, "red") #Red Team Fields
    create_input_fields(720, 88, "green") #Green Team Fields

    buttons = [
        (0, "F1\nEdit\nGame"),
        (120, "F2\nGame\nParameters"),
        (318, "F3\nStart\nGame"),
        (516, "F5\nPreEntered\nGames"),
        (714, "F7\nChange\nIP Address"),
        (912, "F8\nView\nGame"),
        (1110, "F10\nFlick\nSync"),
        (1230, "F12\nClear\nGame")
    ]

    #Function for buttons added here
    for x, text in buttons:
        btn = Button(frame, text=text, font=("Helvetica", 11), fg="#00B300", bg="#1C2920", relief="raised", command=lambda t=text: on_button_click(t))
        btn.place(x=x, y=710, width=120, height=120)

    canvas.create_rectangle(0, 830, 1350, 870, fill="#808A87")
    canvas.create_text(675, 850, text="<Del> to Delete Player, <ins> to Manually Insert, or edit codename", font=("Helvetica", 12), fill="#DCDDDE")
    canvas.scale("all", 0, 0, 1.0, 1.0)
    entry_screen_window.protocol("WM_DELETE_WINDOW", root.destroy)
