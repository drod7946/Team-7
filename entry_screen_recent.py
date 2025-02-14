from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
entry_root = customtkinter.CTk()

entry_root.title("Entry Terminal")
entry_root.geometry("1350x900")

# Get the screen width and height
screen_width = entry_root.winfo_screenwidth()
screen_height = entry_root.winfo_screenheight()

# Calculate the x and y coordinates to center the window
center_x = int(screen_width / 2 - 1350 / 2)
center_y = int(screen_height / 2 - 900 / 2)

# Set the window's position
entry_root.geometry(f"1350x900+{center_x}+{center_y}")

label = customtkinter.CTkLabel(entry_root, text="Edit Current Game", font=("Helvetica", 18, "bold"), text_color="blue")
label.pack(pady=0)

window_bg = entry_root.cget("bg")
scale_factor = 0.8

frame = Frame(entry_root)
frame.pack(fill="both", expand=True, anchor="n")

canvas = Canvas(frame, width=int(1350 * scale_factor), height=int(900 * scale_factor), bg=window_bg, highlightthickness=0)
canvas.pack(fill="both", expand=True, anchor="n")

# x1, y1, x2, y2 ; red box
canvas.create_rectangle(50, 10, 650, 850, fill="red", outline="red")

canvas.create_rectangle(250, 20, 450, 60, outline="white")
canvas.create_text(350, 40, text="RED TEAM", font=("Helvetica", 14), fill="white")

canvas.create_text(80, 88, text=">>", font=("Helvetica", 18), fill="white") # number
canvas.create_rectangle(108, 80, 125, 97, outline="white") # check box
canvas.create_text(137, 88, text="0", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(150, 70, 355, 105, fill="white", outline="white")
canvas.create_rectangle(360, 70, 640, 105, fill="white", outline="white")

canvas.create_rectangle(108, 120, 125, 137, outline="white") # check box
canvas.create_text(137, 128, text="1", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(150, 110, 355, 145, fill="white", outline="white")
canvas.create_rectangle(360, 110, 640, 145, fill="white", outline="white")

canvas.create_rectangle(108, 160, 125, 177, outline="white") # check box
canvas.create_text(137, 168, text="2", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(150, 150, 355, 185, fill="white", outline="white")
canvas.create_rectangle(360, 150, 640, 185, fill="white", outline="white")

canvas.create_rectangle(108, 200, 125, 217, outline="white") # check box
canvas.create_text(137, 208, text="3", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(150, 190, 355, 225, fill="white", outline="white")
canvas.create_rectangle(360, 190, 640, 225, fill="white", outline="white")

canvas.create_rectangle(108, 240, 125, 257, outline="white") # check box
canvas.create_text(137, 248, text="4", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(150, 230, 355, 265, fill="white", outline="white")
canvas.create_rectangle(360, 230, 640, 265, fill="white", outline="white")

canvas.create_rectangle(108, 280, 125, 297, outline="white") # check box
canvas.create_text(137, 288, text="5", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(150, 270, 355, 305, fill="white", outline="white")
canvas.create_rectangle(360, 270, 640, 305, fill="white", outline="white")

canvas.create_rectangle(108, 320, 125, 337, outline="white") # check box
canvas.create_text(137, 328, text="6", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(150, 310, 355, 345, fill="white", outline="white")
canvas.create_rectangle(360, 310, 640, 345, fill="white", outline="white")

canvas.create_rectangle(108, 360, 125, 377, outline="white") # check box
canvas.create_text(137, 368, text="7", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(150, 350, 355, 385, fill="white", outline="white")
canvas.create_rectangle(360, 350, 640, 385, fill="white", outline="white")

canvas.create_rectangle(108, 400, 125, 417, outline="white") # check box
canvas.create_text(137, 408, text="8", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(150, 390, 355, 425, fill="white", outline="white")
canvas.create_rectangle(360, 390, 640, 425, fill="white", outline="white")

canvas.create_rectangle(108, 440, 125, 457, outline="white") # check box
canvas.create_text(137, 448, text="9", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(150, 430, 355, 465, fill="white", outline="white")
canvas.create_rectangle(360, 430, 640, 465, fill="white", outline="white")

canvas.create_rectangle(108, 480, 125, 497, outline="white") # check box
canvas.create_text(137, 488, text="10", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(150, 470, 355, 505, fill="white", outline="white")
canvas.create_rectangle(360, 470, 640, 505, fill="white", outline="white")

canvas.create_rectangle(108, 520, 125, 537, outline="white") # check box
canvas.create_text(137, 528, text="11", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(150, 510, 355, 545, fill="white", outline="white")
canvas.create_rectangle(360, 510, 640, 545, fill="white", outline="white")

canvas.create_rectangle(108, 560, 125, 577, outline="white") # check box
canvas.create_text(137, 568, text="12", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(150, 550, 355, 585, fill="white", outline="white")
canvas.create_rectangle(360, 550, 640, 585, fill="white", outline="white")

canvas.create_rectangle(108, 600, 125, 617, outline="white") # check box
canvas.create_text(137, 608, text="13", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(150, 590, 355, 625, fill="white", outline="white")
canvas.create_rectangle(360, 590, 640, 625, fill="white", outline="white")

canvas.create_rectangle(108, 640, 125, 657, outline="white") # check box
canvas.create_text(137, 648, text="14", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(150, 630, 355, 665, fill="white", outline="white")
canvas.create_rectangle(360, 630, 640, 665, fill="white", outline="white")

canvas.create_rectangle(108, 680, 125, 697, outline="white") # check box
canvas.create_text(137, 688, text="15", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(150, 670, 355, 705, fill="white", outline="white")
canvas.create_rectangle(360, 670, 640, 705, fill="white", outline="white")

canvas.create_rectangle(108, 720, 125, 737, outline="white") # check box
canvas.create_text(137, 728, text="16", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(150, 710, 355, 745, fill="white", outline="white")
canvas.create_rectangle(360, 710, 640, 745, fill="white", outline="white")

canvas.create_rectangle(108, 760, 125, 777, outline="white") # check box
canvas.create_text(137, 768, text="17", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(150, 750, 355, 785, fill="white", outline="white")
canvas.create_rectangle(360, 750, 640, 785, fill="white", outline="white")

canvas.create_rectangle(108, 800, 125, 817, outline="white") # check box
canvas.create_text(137, 808, text="18", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(150, 790, 355, 825, fill="white", outline="white")
canvas.create_rectangle(360, 790, 640, 825, fill="white", outline="white")

# green box
canvas.create_rectangle(660, 10, 1260, 850, fill="green", outline="green") 

canvas.create_rectangle(860, 20, 1060, 60, outline="white")
canvas.create_text(960, 40, text="GREEN TEAM", font=("Helvetica", 14), fill="white")

canvas.create_rectangle(710, 80, 727, 97, outline="white") # check box
canvas.create_text(740, 88, text="0", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(760, 70, 965, 105, fill="white", outline="white")
canvas.create_rectangle(970, 70, 1250, 105, fill="white", outline="white")

canvas.create_rectangle(710, 120, 727, 137, outline="white") # check box
canvas.create_text(740, 128, text="1", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(760, 110, 965, 145, fill="white", outline="white")
canvas.create_rectangle(970, 110, 1250, 145, fill="white", outline="white")

canvas.create_rectangle(710, 160, 727, 177, outline="white") # check box
canvas.create_text(740, 168, text="2", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(760, 150, 965, 185, fill="white", outline="white")
canvas.create_rectangle(970, 150, 1250, 185, fill="white", outline="white")

canvas.create_rectangle(710, 200, 727, 217, outline="white") # check box
canvas.create_text(740, 208, text="3", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(760, 190, 965, 225, fill="white", outline="white")
canvas.create_rectangle(970, 190, 1250, 225, fill="white", outline="white")

canvas.create_rectangle(710, 240, 727, 257, outline="white") # check box
canvas.create_text(740, 248, text="4", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(760, 230, 965, 265, fill="white", outline="white")
canvas.create_rectangle(970, 230, 1250, 265, fill="white", outline="white")

canvas.create_rectangle(710, 280, 727, 297, outline="white") # check box
canvas.create_text(740, 288, text="5", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(760, 270, 965, 305, fill="white", outline="white")
canvas.create_rectangle(970, 270, 1250, 305, fill="white", outline="white")

canvas.create_rectangle(710, 320, 727, 337, outline="white") # check box
canvas.create_text(740, 328, text="6", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(760, 310, 965, 345, fill="white", outline="white")
canvas.create_rectangle(970, 310, 1250, 345, fill="white", outline="white")

canvas.create_rectangle(710, 360, 727, 377, outline="white") # check box
canvas.create_text(740, 368, text="7", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(760, 350, 965, 385, fill="white", outline="white")
canvas.create_rectangle(970, 350, 1250, 385, fill="white", outline="white")

canvas.create_rectangle(710, 400, 727, 417, outline="white") # check box
canvas.create_text(740, 408, text="8", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(760, 390, 965, 425, fill="white", outline="white")
canvas.create_rectangle(970, 390, 1250, 425, fill="white", outline="white")

canvas.create_rectangle(710, 440, 727, 457, outline="white") # check box
canvas.create_text(740, 448, text="9", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(760, 430, 965, 465, fill="white", outline="white")
canvas.create_rectangle(970, 430, 1250, 465, fill="white", outline="white")

canvas.create_rectangle(710, 480, 727, 497, outline="white") # check box
canvas.create_text(740, 488, text="10", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(760, 470, 965, 505, fill="white", outline="white")
canvas.create_rectangle(970, 470, 1250, 505, fill="white", outline="white")

canvas.create_rectangle(710, 520, 727, 537, outline="white") # check box
canvas.create_text(740, 528, text="11", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(760, 510, 965, 545, fill="white", outline="white")
canvas.create_rectangle(970, 510, 1250, 545, fill="white", outline="white")

canvas.create_rectangle(710, 560, 727, 577, outline="white") # check box
canvas.create_text(740, 568, text="12", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(760, 550, 965, 585, fill="white", outline="white")
canvas.create_rectangle(970, 550, 1250, 585, fill="white", outline="white")

canvas.create_rectangle(710, 600, 727, 617, outline="white") # check box
canvas.create_text(740, 608, text="13", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(760, 590, 965, 625, fill="white", outline="white")
canvas.create_rectangle(970, 590, 1250, 625, fill="white", outline="white")

canvas.create_rectangle(710, 640, 727, 657, outline="white") # check box
canvas.create_text(740, 648, text="14", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(760, 630, 965, 665, fill="white", outline="white")
canvas.create_rectangle(970, 630, 1250, 665, fill="white", outline="white")

canvas.create_rectangle(710, 680, 727, 697, outline="white") # check box
canvas.create_text(740, 688, text="15", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(760, 670, 965, 705, fill="white", outline="white")
canvas.create_rectangle(970, 670, 1250, 705, fill="white", outline="white")

canvas.create_rectangle(710, 720, 727, 737, outline="white") # check box
canvas.create_text(740, 728, text="16", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(760, 710, 965, 745, fill="white", outline="white")
canvas.create_rectangle(970, 710, 1250, 745, fill="white", outline="white")

canvas.create_rectangle(710, 760, 727, 777, outline="white") # check box
canvas.create_text(740, 768, text="17", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(760, 750, 965, 785, fill="white", outline="white")
canvas.create_rectangle(970, 750, 1250, 785, fill="white", outline="white")

canvas.create_rectangle(710, 800, 727, 817, outline="white") # check box
canvas.create_text(740, 808, text="18", font=("Helvetica", 14), fill="white") # number
canvas.create_rectangle(760, 790, 965, 825, fill="white", outline="white")
canvas.create_rectangle(970, 790, 1250, 825, fill="white", outline="white")

canvas.create_rectangle(425, 850, 875, 885, fill="grey", outline="grey")
canvas.create_text(650, 867, text="Game Mode: Standard public mode", font=("Helvetica", 14, "bold"), fill="white")

canvas.create_rectangle(0, 1050, 120, 1170, outline="grey") # check box
canvas.create_text(60, 1100, text="F1\nEdit\nGame", font=("Helvetica", 11), fill="lime", anchor="center") # number

canvas.create_rectangle(120, 1050, 240, 1170, outline="grey") # check box
canvas.create_text(180, 1100, text="F2\nGame\nParameters", font=("Helvetica", 11), fill="lime", anchor="center") # number

canvas.create_rectangle(240, 1050, 360, 1170, outline="grey") # check box
canvas.create_text(300, 1100, text="F3\nStart\nGame", font=("Helvetica", 11), fill="lime", anchor="center") # number

canvas.create_rectangle(600, 1050, 720, 1170, outline="grey") # check box
canvas.create_text(660, 1100, text="F5\nPreEntered\nGames", font=("Helvetica", 11), fill="lime", anchor="center") # number

canvas.create_rectangle(1050, 1050, 1170, 1170, outline="grey") # check box
canvas.create_text(1110, 1100, text="F7", font=("Helvetica", 11), fill="lime", anchor="center") # number

canvas.create_rectangle(1170, 1050, 1290, 1170, outline="grey") # check box
canvas.create_text(1230, 1100, text="F8\nView\nGame", font=("Helvetica", 11), fill="lime", anchor="center") # number

canvas.create_rectangle(1400, 1050, 1520, 1170, outline="grey") # check box
canvas.create_text(1460, 1100, text="F10\nFlick\nSync", font=("Helvetica", 11), fill="lime", anchor="center") # number

canvas.create_rectangle(1985, 1050, 2105, 1170, outline="grey") # check box
canvas.create_text(2050, 1100, text="F12\nClear\nGame", font=("Helvetica", 11), fill="lime", anchor="center") # number

canvas.create_rectangle(0, 1170, 2110, 1210, fill="grey")  # Footer background
canvas.create_text(1025, 1190, text="<Del> to Delete Player, <ins> to Manually Insert, or edit codename", font=("Helvetica", 12), fill="white")

canvas.scale("all", 0, 0, scale_factor, scale_factor)

entry_root.mainloop()
