from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
entry_root = customtkinter.CTk()

entry_root.title("Entry Terminal")
entry_root.geometry("600x400")

label = customtkinter.CTkLabel(entry_root, text="Edit Current Game", font=("Helvetica", 18, "bold"), text_color="blue")
label.pack(pady=10)

window_bg = entry_root.cget("bg")

canvas = Canvas(entry_root, width=1300, height=1000, bg=window_bg, highlightthickness=0)  
canvas.pack()

# x1, y1, x2, y2 ; red box
canvas.create_rectangle(50, 10, 650, 850, fill="red", outline="red")

canvas.create_rectangle(250, 20, 450, 60, outline="white")
canvas.create_text(350, 40, text="RED TEAM", font=("Helvetica", 14), fill="white")

canvas.create_rectangle(150, 70, 355, 105, fill="white", outline="white")
canvas.create_rectangle(360, 70, 640, 105, fill="white", outline="white")

canvas.create_rectangle(150, 110, 355, 145, fill="white", outline="white")
canvas.create_rectangle(360, 110, 640, 145, fill="white", outline="white")

canvas.create_rectangle(150, 150, 355, 185, fill="white", outline="white")
canvas.create_rectangle(360, 150, 640, 185, fill="white", outline="white")

canvas.create_rectangle(150, 190, 355, 225, fill="white", outline="white")
canvas.create_rectangle(360, 190, 640, 225, fill="white", outline="white")

canvas.create_rectangle(150, 230, 355, 265, fill="white", outline="white")
canvas.create_rectangle(360, 230, 640, 265, fill="white", outline="white")

canvas.create_rectangle(150, 270, 355, 305, fill="white", outline="white")
canvas.create_rectangle(360, 270, 640, 305, fill="white", outline="white")

canvas.create_rectangle(150, 310, 355, 345, fill="white", outline="white")
canvas.create_rectangle(360, 310, 640, 345, fill="white", outline="white")

canvas.create_rectangle(150, 350, 355, 385, fill="white", outline="white")
canvas.create_rectangle(360, 350, 640, 385, fill="white", outline="white")

canvas.create_rectangle(150, 390, 355, 425, fill="white", outline="white")
canvas.create_rectangle(360, 390, 640, 425, fill="white", outline="white")

canvas.create_rectangle(150, 430, 355, 465, fill="white", outline="white")
canvas.create_rectangle(360, 430, 640, 465, fill="white", outline="white")

canvas.create_rectangle(150, 470, 355, 505, fill="white", outline="white")
canvas.create_rectangle(360, 470, 640, 505, fill="white", outline="white")

canvas.create_rectangle(150, 510, 355, 545, fill="white", outline="white")
canvas.create_rectangle(360, 510, 640, 545, fill="white", outline="white")

canvas.create_rectangle(150, 550, 355, 585, fill="white", outline="white")
canvas.create_rectangle(360, 550, 640, 585, fill="white", outline="white")

canvas.create_rectangle(150, 590, 355, 625, fill="white", outline="white")
canvas.create_rectangle(360, 590, 640, 625, fill="white", outline="white")

canvas.create_rectangle(150, 630, 355, 665, fill="white", outline="white")
canvas.create_rectangle(360, 630, 640, 665, fill="white", outline="white")

canvas.create_rectangle(150, 670, 355, 705, fill="white", outline="white")
canvas.create_rectangle(360, 670, 640, 705, fill="white", outline="white")

canvas.create_rectangle(150, 710, 355, 745, fill="white", outline="white")
canvas.create_rectangle(360, 710, 640, 745, fill="white", outline="white")

canvas.create_rectangle(150, 750, 355, 785, fill="white", outline="white")
canvas.create_rectangle(360, 750, 640, 785, fill="white", outline="white")

canvas.create_rectangle(150, 790, 355, 825, fill="white", outline="white")
canvas.create_rectangle(360, 790, 640, 825, fill="white", outline="white")

# green box
canvas.create_rectangle(660, 10, 1260, 850, fill="green", outline="green") 

canvas.create_rectangle(860, 20, 1060, 60, outline="white")
canvas.create_text(960, 40, text="GREEN TEAM", font=("Helvetica", 14), fill="white")

canvas.create_rectangle(760, 70, 965, 105, fill="white", outline="white")
canvas.create_rectangle(970, 70, 1250, 105, fill="white", outline="white")

canvas.create_rectangle(760, 110, 965, 145, fill="white", outline="white")
canvas.create_rectangle(970, 110, 1250, 145, fill="white", outline="white")

canvas.create_rectangle(760, 150, 965, 185, fill="white", outline="white")
canvas.create_rectangle(970, 150, 1250, 185, fill="white", outline="white")

canvas.create_rectangle(760, 190, 965, 225, fill="white", outline="white")
canvas.create_rectangle(970, 190, 1250, 225, fill="white", outline="white")

canvas.create_rectangle(760, 230, 965, 265, fill="white", outline="white")
canvas.create_rectangle(970, 230, 1250, 265, fill="white", outline="white")

canvas.create_rectangle(760, 270, 965, 305, fill="white", outline="white")
canvas.create_rectangle(970, 270, 1250, 305, fill="white", outline="white")

canvas.create_rectangle(760, 310, 965, 345, fill="white", outline="white")
canvas.create_rectangle(970, 310, 1250, 345, fill="white", outline="white")

canvas.create_rectangle(760, 350, 965, 385, fill="white", outline="white")
canvas.create_rectangle(970, 350, 1250, 385, fill="white", outline="white")

canvas.create_rectangle(760, 390, 965, 425, fill="white", outline="white")
canvas.create_rectangle(970, 390, 1250, 425, fill="white", outline="white")

canvas.create_rectangle(760, 430, 965, 465, fill="white", outline="white")
canvas.create_rectangle(970, 430, 1250, 465, fill="white", outline="white")

canvas.create_rectangle(760, 470, 965, 505, fill="white", outline="white")
canvas.create_rectangle(970, 470, 1250, 505, fill="white", outline="white")

canvas.create_rectangle(760, 510, 965, 545, fill="white", outline="white")
canvas.create_rectangle(970, 510, 1250, 545, fill="white", outline="white")

canvas.create_rectangle(760, 550, 965, 585, fill="white", outline="white")
canvas.create_rectangle(970, 550, 1250, 585, fill="white", outline="white")

canvas.create_rectangle(760, 590, 965, 625, fill="white", outline="white")
canvas.create_rectangle(970, 590, 1250, 625, fill="white", outline="white")

canvas.create_rectangle(760, 630, 965, 665, fill="white", outline="white")
canvas.create_rectangle(970, 630, 1250, 665, fill="white", outline="white")

canvas.create_rectangle(760, 670, 965, 705, fill="white", outline="white")
canvas.create_rectangle(970, 670, 1250, 705, fill="white", outline="white")

canvas.create_rectangle(760, 710, 965, 745, fill="white", outline="white")
canvas.create_rectangle(970, 710, 1250, 745, fill="white", outline="white")

canvas.create_rectangle(760, 750, 965, 785, fill="white", outline="white")
canvas.create_rectangle(970, 750, 1250, 785, fill="white", outline="white")

canvas.create_rectangle(760, 790, 965, 825, fill="white", outline="white")
canvas.create_rectangle(970, 790, 1250, 825, fill="white", outline="white")

canvas.create_rectangle(475, 850, 825, 885, fill="grey", outline="grey")
canvas.create_text(650, 867, text="Game Mode: Standard public mode", font=("Helvetica", 14, "bold"), fill="white")



entry_root.mainloop()
