from tkinter import *
import customtkinter
import tkinter as tk
import psycopg2
from play_action_display import show_countdown

from udp_utils import set_target_ip, get_target_ip
from tkinter import simpledialog, messagebox

# Database connection function
def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname="photon",
            # user="student", 
            # password="student", 
            # host="localhost", 
            # port="5432"
        )
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

# Function to insert player and equipment ID into database
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
            # for return, make a new function for a pop up to add new player?
            return result[0] if result else None
        except Exception as e:
            print(f"Error fetching player: {e}")
            return None
        finally:
            cursor.close()
            connection.close()

def show_entry_screen(root):
    customtkinter.set_appearance_mode("dark")
    entry_screen_window = customtkinter.CTkToplevel(root)

    entry_screen_window.title("Entry Terminal")
    entry_screen_window.geometry("1350x900")

    def on_button_click(text):
        print(f"Button {text} clicked")
        if text == "F5\nPreEntered\nGames":
            show_countdown()
        if text == "F12\nClear\nGame":
            clear_entries()
        if text == "F7\nChange\nIP Address":
            change_ip_popup()
    
    # hardware ID code  
    # I think this where we should make a new function to determine what happens for adding a new player  
    def on_key_pressed(event):
        if event.keysym == "Return":
            for entry1, entry2 in entry_fields:
                player_id = entry1.get().strip()
                codename = entry2.get().strip()
                if player_id:
                    existing_codename = get_player_codename(player_id)
                    if existing_codename:
                        #Makes 2nd textbox editable temporarily
                        entry2.config(state="normal")
                        entry2.delete(0, tk.END)
                        entry2.insert(0, existing_codename)
                        entry2.config(state="readonly")
                        print(f"Existing player found: {player_id} → {existing_codename}")
                    elif not codename:
                        # Prompt user for codename
                        new_codename = simpledialog.askstring("New Player", f"Enter codename for new player ID: {player_id}")
                        if new_codename:
                            insert_player(player_id, new_codename)
                            entry2.config(state="normal")
                            entry2.insert(0, new_codename)
                            entry2.config(state="readonly")
                            print(f"New player added: {player_id} → {new_codename}")
                    elif codename:
                        insert_player(player_id, codename)
                        print(f"Inserted new player: {player_id} → {codename}")
       
        if event.keysym == "F1":
            print("F1 pressed")
        if event.keysym == "F2":
            print("F2 pressed")
        if event.keysym == "F3":
            print("F3 pressed")
        if event.keysym == "F5":
            show_countdown()
            print("F5 pressed")
        if event.keysym == "F7":
            change_ip_popup()
            print("F7 pressed")
        if event.keysym == "F8":
            print("F8 pressed")
        if event.keysym == "F10":
            print("F10 pressed")
        if event.keysym == "F12":
            print("F12 pressed")
            clear_entries()
            
            
    entry_screen_window.bind("<Return>", on_key_pressed)
    		
    def clear_entries():
        print('Clearing all player entries')
        for entry1, entry2 in entry_fields:
            entry1.delete(0, tk.END)
            entry2.config(state="normal")
            entry2.delete(0, tk.END)
            entry2.config(state="readonly")

    def change_ip_popup():
        current_ip = get_target_ip()
        new_ip = simpledialog.askstring("Set Target IP", f"Current IP: {current_ip}\nEnter new target IP address:")

        if new_ip:
            # Basic validation: IP should have 4 octets
            parts = new_ip.strip().split(".")
            if len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts):
                set_target_ip(new_ip.strip())
                messagebox.showinfo("IP Address Set", f"New IP Address: {new_ip.strip()}")
            else:
                messagebox.showerror("Invalid IP", "Please enter a valid IPv4 address.")

    # Get the screen width and height
    screen_width = entry_screen_window.winfo_screenwidth()
    screen_height = entry_screen_window.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    center_x = int(screen_width / 2 - 1350 / 2)
    center_y = int(screen_height / 2 - 900 / 2)

    # Set the window's position
    entry_screen_window.geometry(f"1350x900+{center_x}+{center_y}")
    entry_screen_window.update()

    label = customtkinter.CTkLabel(entry_screen_window, text="Edit Current Game", font=("Helvetica", 18, "bold"), text_color="#99AAFF")
    label.pack(pady=0)

    window_bg = entry_screen_window.cget("bg")
    #scale_factor = 0.8

    frame = Frame(entry_screen_window)
    frame.pack(fill="both", expand=True, anchor="n")

    canvas = Canvas(frame, width=int(1350), height=int(900), bg=window_bg, highlightthickness=0)
    canvas.pack(fill="both", expand=True, anchor="n")

    # red box (x1, y1, x2, y2) ; #DCDDDE = darkish white
    canvas.create_rectangle(40, 10, 640, 600, fill="#B30000", outline="#B30000")
    canvas.create_rectangle(240, 20, 440, 60, outline="#DCDDDE")
    canvas.create_text(340, 40, text="RED TEAM", font=("Helvetica", 14), fill="#DCDDDE")

    # green box
    canvas.create_rectangle(710, 10, 1310, 600, fill="#008000", outline="#008000") 
    canvas.create_rectangle(910, 20, 1110, 60, outline="#DCDDDE")
    canvas.create_text(1010, 40, text="GREEN TEAM", font=("Helvetica", 14), fill="#DCDDDE")

    # grey rectangle
    canvas.create_rectangle(445, 600, 905, 635, fill="#808A87", outline="#808A87")
    canvas.create_text(675, 617, text="Game Mode: Standard public mode", font=("Helvetica", 14, "bold"), fill="#DCDDDE")

    entry_fields = []

    def create_input_fields(start_x, start_y):
        for i in range(16):
            y_offset = start_y + (i * 30)
            canvas.create_rectangle(start_x, y_offset, start_x + 17, y_offset + 17, outline="#DCDDDE") # check box
            canvas.create_text(start_x + 35, y_offset + 8, text=str(i), font=("Helvetica", 14), fill="#DCDDDE") # number
            
            entry1 = Entry(entry_screen_window, font=("Helvetica", 14), bg="#DCDDDE", width=25)
            entry2 = Entry(entry_screen_window, font=("Helvetica", 14), bg="#DCDDDE", width=25, state="readonly")
            
            canvas.create_window(start_x + 50, y_offset + 8, window=entry1, anchor=W)
            canvas.create_window(start_x + 250, y_offset + 8, window=entry2, anchor=W)
            
            entry_fields.append((entry1, entry2))

    create_input_fields(50, 88) # Red Team Fields
    create_input_fields(720, 88) # Green Team Fields

    entry_screen_window.update_idletasks()

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

    # Function for buttons added here
    for x, text in buttons:
        btn = Button(frame, text=text, font=("Helvetica", 11), fg="#00B300", bg="#1C2920", relief="raised", command=lambda t=text: on_button_click(t))
        btn.place(x=x, y=710, width=120, height=120)

    entry_screen_window.bind_all("<F1>", on_key_pressed)
    entry_screen_window.bind_all("<F2>", on_key_pressed)
    entry_screen_window.bind_all("<F3>", on_key_pressed)
    entry_screen_window.bind_all("<F5>", on_key_pressed)
    entry_screen_window.bind_all("<F7>", on_key_pressed)
    entry_screen_window.bind_all("<F8>", on_key_pressed)
    entry_screen_window.bind_all("<F10>", on_key_pressed)
    entry_screen_window.bind_all("<F12>", on_key_pressed)

    canvas.create_rectangle(0, 830, 1350, 870, fill="#808A87")  # Footer background
    canvas.create_text(675, 850, text="<Del> to Delete Player, <ins> to Manually Insert, or edit codename", font=("Helvetica", 12), fill="#DCDDDE")

    canvas.scale("all", 0, 0, 1.0, 1.0)

    entry_screen_window.protocol("WM_DELETE_WINDOW", root.destroy)
