import psycopg2
import tkinter as tk
from tkinter import messagebox

# Define connection parameters
connection_params = {
    'dbname': 'photon',
    'user': 'student',
    #'password': 'student',
    #'host': 'localhost',
    #'port': '5432'
}

def fetch_player_names():
    """Fetch player names from the database."""
    try:
        conn = psycopg2.connect(**connection_params)
        cursor = conn.cursor()

        # Fetch player names from the database
        cursor.execute("SELECT id, codename FROM players;")
        rows = cursor.fetchall()
        return rows  # Return as list of tuples (id, name)

    except Exception as error:
        print(f"Error connecting to PostgreSQL database: {error}")
        return []

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def update_player_name(player_id, new_name):
    """Update player name in the database."""
    try:
        conn = psycopg2.connect(**connection_params)
        cursor = conn.cursor()

        # Update player name in the database
        cursor.execute("UPDATE players SET codename = %s WHERE id = %s;", (new_name, player_id))
        conn.commit()
        messagebox.showinfo("Success", "Player name updated successfully!")

    except Exception as error:
        messagebox.showerror("Error", f"Failed to update player name: {error}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def on_player_select(event, listbox, entry, selected_player_label):
    """Handle player selection from the listbox."""
    # Get the selected player from the listbox
    selected_player = listbox.get(listbox.curselection())
    selected_player_label.config(text=f"Editing: {selected_player[1]}")
    entry.delete(0, tk.END)  # Clear entry
    entry.insert(0, selected_player[1])  # Insert selected name into entry

def create_edit_screen():
    """Create the Tkinter edit screen for editing player names."""
    root = tk.Tk()
    root.title("Edit Player Names")

    # Create the frame for the listbox and scrollbars
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    # Fetch player names from the database
    player_data = fetch_player_names()

    # Listbox to display player names
    listbox = tk.Listbox(frame, height=10, width=50, selectmode=tk.SINGLE)
    for player in player_data:
        listbox.insert(tk.END, player)  # Insert tuples (id, name)
    listbox.pack(side=tk.LEFT, fill=tk.Y)

    # Scrollbar for listbox
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    # Label for selected player
    selected_player_label = tk.Label(root, text="Select a player to edit", font=("Helvetica", 12))
    selected_player_label.pack(pady=10)

    # Entry field to edit the selected player's name
    entry = tk.Entry(root, font=("Helvetica", 14))
    entry.pack(pady=10)

    # Button to update player name
    def update_name():
        selected_player = listbox.get(listbox.curselection())
        new_name = entry.get()
        if new_name:
            update_player_name(selected_player[0], new_name)  # Pass id and new name
            listbox.delete(listbox.curselection())  # Remove the old entry
            listbox.insert(listbox.curselection(), (selected_player[0], new_name))  # Update in listbox
        else:
            messagebox.showwarning("Input Error", "Please enter a new name.")

    update_button = tk.Button(root, text="Update Name", font=("Helvetica", 12), command=update_name)
    update_button.pack(pady=10)

    # Bind select event on the listbox to display the selected player's name in the entry
    listbox.bind('<<ListboxSelect>>', lambda event: on_player_select(event, listbox, entry, selected_player_label))

    root.mainloop()

if __name__ == "__main__":
    create_edit_screen()
