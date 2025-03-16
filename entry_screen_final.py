from tkinter import *
import customtkinter
from play_action_display import show_countdown

def show_entry_screen(root):
    customtkinter.set_appearance_mode("dark")
    entry_screen_window = customtkinter.CTkToplevel(root)

    entry_screen_window.title("Entry Terminal")
    entry_screen_window.geometry("1600x900")  
    entry_screen_window.resizable(True, True)

    def clear_entries():
        print('Clearing all player entries')
        for entry1, entry2 in entry_fields:
            entry1.delete(0, END)
            entry2.delete(0, END)

    def on_button_click(text):
        print(f"Button {text} clicked")
        if text == "F5\nPreEntered\nGames":
            entry_screen_window.destroy()  
            show_countdown()  
        if text == "F12\nClear\nGame":
            clear_entries()
    def on_key_press(event):
        if event.keysym == "F1":
            print("F1 pressed")
        if event.keysym == "F2":
            print("F2 pressed")
        if event.keysym == "F3":
            print("F3 pressed")
        if event.keysym == "F5":
            print("F5 pressed - Closing Entry Terminal & Launching Play Action Display")
            entry_screen_window.destroy()
            show_countdown()
        if event.keysym == "F7":
            print("F7 pressed")
        if event.keysym == "F8":
            print("F8 pressed")
        if event.keysym == "F10":
            print("F10 pressed")
        if event.keysym == "F12":
            print("F12 pressed")
            clear_entries()

    # Get the screen width and height
    screen_width = entry_screen_window.winfo_screenwidth()
    screen_height = entry_screen_window.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    center_x = int(screen_width / 2 - 1600 / 2)
    center_y = int(screen_height / 2 - 900 / 2)

    # Set the window's position
    entry_screen_window.geometry(f"1600x900+{center_x}+{center_y}")

    label = customtkinter.CTkLabel(entry_screen_window, text="Edit Current Game", font=("Helvetica", 18, "bold"), text_color="#99AAFF")
    label.pack(pady=0)

    window_bg = entry_screen_window.cget("bg")
    scale_factor = 0.8

    frame = Frame(entry_screen_window)
    frame.pack(fill="both", expand=True, anchor="n")

    canvas = Canvas(frame, width=int(1600 * scale_factor), height=int(900 * scale_factor), bg=window_bg, highlightthickness=0)
    canvas.pack(fill="both", expand=True, anchor="n")

    # Red team box (x1, y1, x2, y2) ; #DCDDDE = darkish white
    canvas.create_rectangle(440, 10, 1040, 850, fill="#B30000", outline="#B30000")
    canvas.create_rectangle(640, 20, 840, 60, outline="#DCDDDE")
    canvas.create_text(740, 40, text="RED TEAM", font=("Helvetica", 14), fill="#DCDDDE")

    # Green Team box
    canvas.create_rectangle(1050, 10, 1650, 850, fill="#008000", outline="#008000") 
    canvas.create_rectangle(1250, 20, 1450, 60, outline="#DCDDDE")
    canvas.create_text(1350, 40, text="GREEN TEAM", font=("Helvetica", 14), fill="#DCDDDE")

    entry_fields = []

    def create_input_fields(start_x, start_y):
        for i in range(19):
            y_offset = start_y + (i * 40)
            canvas.create_rectangle(start_x, y_offset, start_x + 17, y_offset + 17, outline="#DCDDDE") # checkbox
            canvas.create_text(start_x + 35, y_offset + 8, text=str(i), font=("Helvetica", 14), fill="#DCDDDE") # Number
            
            entry1 = Entry(entry_screen_window, font=("Helvetica", 14), bg="#DCDDDE", width=25)
            entry2 = Entry(entry_screen_window, font=("Helvetica", 14), bg="#DCDDDE", width=25)
            
            canvas.create_window(start_x + 50, y_offset + 8, window=entry1, anchor=W)
            canvas.create_window(start_x + 230, y_offset + 8, window=entry2, anchor=W)
            
            entry_fields.append((entry1, entry2))

    create_input_fields(450, 88) # Red Team Fields
    create_input_fields(1060, 88) # Green Team Fields

    buttons = [
        (0, "F1\nEdit\nGame"),
        (120, "F2\nGame\nParameters"),
        (240, "F3\nStart\nGame"),
        (600, "F5\nPreEntered\nGames"),
        (1050, "F7"),
        (1170, "F8\nView\nGame"),
        (1400, "F10\nFlick\nSync"),
        (1575, "F12\nClear\nGame")
    ]

    # Function for buttons added here
    for x, text in buttons:
        btn = Button(frame, text=text, font=("Helvetica", 11), fg="#00B300", bg="#1C2920", relief="raised", command=lambda t=text: on_button_click(t))
        btn.place(x=x, y=818, width=120, height=120)

    entry_screen_window.bind_all("<F1>", on_key_press)
    entry_screen_window.bind_all("<F2>", on_key_press)
    entry_screen_window.bind_all("<F3>", on_key_press)
    entry_screen_window.bind_all("<F5>", on_key_press)
    entry_screen_window.bind_all("<F7>", on_key_press)
    entry_screen_window.bind_all("<F8>", on_key_press)
    entry_screen_window.bind_all("<F10>", on_key_press)
    entry_screen_window.bind_all("<F12>", on_key_press)

    canvas.create_rectangle(0, 1170, 2110, 1210, fill="#808A87")  # Footer background
    canvas.create_text(1025, 1190, text="<Del> to Delete Player, <ins> to Manually Insert, or edit codename", font=("Helvetica", 12), fill="#DCDDDE")

    canvas.scale("all", 0, 0, scale_factor, scale_factor)

    entry_screen_window.protocol("WM_DELETE_WINDOW", entry_screen_window.quit)
